#include "DataFormats/GeometryVector/interface/LocalPoint.h"

#include "SimG4Core/SensitiveDetector/interface/FrameRotation.h"
#include "SimG4Core/Notification/interface/TrackInformation.h"

#include "SimDataFormats/TrackingHit/interface/UpdatablePSimHit.h"
#include "SimDataFormats/SimHitMaker/interface/TrackingSlaveSD.h"

#include "SimG4CMS/Tracker/interface/TkAccumulatingSensitiveDetector.h"
#include "SimG4CMS/Tracker/interface/FakeFrameRotation.h"
#include "SimG4CMS/Tracker/interface/StandardFrameRotation.h"
#include "SimG4CMS/Tracker/interface/TrackerFrameRotation.h"
#include "SimG4CMS/Tracker/interface/TkSimHitPrinter.h"
#include "SimG4CMS/Tracker/interface/TrackerG4SimHitNumberingScheme.h"

#include "FWCore/Framework/interface/ESTransientHandle.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "Geometry/Records/interface/IdealGeometryRecord.h"
#include "Geometry/TrackerNumberingBuilder/interface/GeometricDet.h"
#include "DetectorDescription/Core/interface/DDCompactView.h"

#include "SimG4Core/Notification/interface/TrackInformation.h"
#include "SimG4Core/Notification/interface/G4TrackToParticleID.h"
#include "SimG4Core/Physics/interface/G4ProcessTypeEnumerator.h"

#include "G4Track.hh"
#include "G4StepPoint.hh"
#include "G4VProcess.hh"

#include "G4SystemOfUnits.hh"

#include <vector>
#include <iostream>

#include "FWCore/MessageLogger/interface/MessageLogger.h"

//#define FAKEFRAMEROTATION

static 
TrackerG4SimHitNumberingScheme&
numberingScheme(const DDCompactView& cpv, const GeometricDet& det)
{
   static thread_local TrackerG4SimHitNumberingScheme s_scheme(cpv, det);
   return s_scheme;
}

TkAccumulatingSensitiveDetector::TkAccumulatingSensitiveDetector(const std::string& name, 
								 const DDCompactView & cpv,
								 const SensitiveDetectorCatalog & clg,
								 edm::ParameterSet const & p,
								 const SimTrackManager* manager) : 
  SensitiveTkDetector(name, cpv, clg, p), myRotation(nullptr),theManager(manager),
  numberingScheme_(nullptr),rTracker(1200.*CLHEP::mm),zTracker(3000.*CLHEP::mm),mySimHit(nullptr), 
  lastId(0),lastTrack(0),oldVolume(nullptr),px(0.0f),py(0.0f),pz(0.0f),eventno(0),pname("")
{
  edm::ParameterSet m_TrackerSD = p.getParameter<edm::ParameterSet>("TrackerSD");
  allowZeroEnergyLoss = m_TrackerSD.getParameter<bool>("ZeroEnergyLoss");
  neverAccumulate     = m_TrackerSD.getParameter<bool>("NeverAccumulate");
  printHits           = m_TrackerSD.getParameter<bool>("PrintHits");
  theTofLimit            = m_TrackerSD.getParameter<double>("ElectronicSigmaInNanoSeconds")*3*CLHEP::ns; // 3 sigma
  energyCut           = m_TrackerSD.getParameter<double>("EnergyThresholdForPersistencyInGeV")*CLHEP::GeV; //default must be 0.5
  energyHistoryCut    = m_TrackerSD.getParameter<double>("EnergyThresholdForHistoryInGeV")*CLHEP::GeV;//default must be 0.05
  rTracker2 = rTracker*rTracker;

  // No Rotation given in input, automagically choose one based upon the name
  std::string rotType;
  if (name.find("TrackerHits") != std::string::npos) {
    myRotation = new TrackerFrameRotation();
    rotType = "TrackerFrameRotation";
  } else {
    // Just in case (test beam etc)
    myRotation = new StandardFrameRotation();
    rotType = "StandardFrameRotation";
  }
#ifdef FAKEFRAMEROTATION
  delete myRotation;
  myRotation = new FakeFrameRotation();
  rotType = "FakeFrameRotation";
#endif

  edm::LogInfo("TrackerSimInfo")<<" TkAccumulatingSensitiveDetector: " 
                                <<" Criteria for Saving Tracker SimTracks: \n"
                                <<" History: "<<energyHistoryCut<< " MeV; Persistency: "
                                << energyCut<<" MeV;  TofLimit: " << theTofLimit << " ns"
				<<"\n FrameRotation type " << rotType
				<<" rTracker(cm)= " << rTracker/CLHEP::cm
				<<" zTracker(cm)= " << zTracker/CLHEP::cm
				<<" allowZeroEnergyLoss: " << allowZeroEnergyLoss
				<<" neverAccumulate: " << neverAccumulate
				<<" printHits: " << printHits;

  slaveLowTof  = new TrackingSlaveSD(name+"LowTof");
  slaveHighTof = new TrackingSlaveSD(name+"HighTof");
  
  std::vector<std::string> temp;
  temp.push_back(slaveLowTof->name());
  temp.push_back(slaveHighTof->name());
  setNames(temp);  

  theG4ProcessTypeEnumerator = new G4ProcessTypeEnumerator;
  myG4TrackToParticleID = new G4TrackToParticleID;
}

TkAccumulatingSensitiveDetector::~TkAccumulatingSensitiveDetector() 
{ 
  delete slaveLowTof;
  delete slaveHighTof;
  delete theG4ProcessTypeEnumerator;
  delete myG4TrackToParticleID;
}

bool TkAccumulatingSensitiveDetector::ProcessHits(G4Step * aStep, G4TouchableHistory *)
{
    LogDebug("TrackerSimDebug")<< " Entering a new Step " << aStep->GetTotalEnergyDeposit() << " " 
	 << aStep->GetPreStepPoint()->GetPhysicalVolume()->GetLogicalVolume()->GetName();

    if (aStep->GetTotalEnergyDeposit()>0. || allowZeroEnergyLoss)
    {
      if (!mySimHit) 
	{
	  createHit(aStep);
	} 
      else if(neverAccumulate || newHit(aStep))
	{
	  sendHit();
	  createHit(aStep);
	}
      else
	{
	  updateHit(aStep);
	}
      return true;
    }
    return false;
}

uint32_t TkAccumulatingSensitiveDetector::setDetUnitId(const G4Step * step)
{ 
  return numberingScheme_->g4ToNumberingScheme(step->GetPreStepPoint()->GetTouchable());
}

Local3DPoint TkAccumulatingSensitiveDetector::toOrcaRef(const Local3DPoint& in)
{
  return myRotation->transformPoint(in);
}

void TkAccumulatingSensitiveDetector::update(const BeginOfTrack *bot){
  const G4Track* gTrack = (*bot)();
#ifdef DUMPPROCESSES
  edm::LogInfo("TrackerSimInfo") <<" -> process creator pointer "<<gTrack->GetCreatorProcess();
  if (gTrack->GetCreatorProcess()) {
    edm::LogInfo("TrackerSimInfo")<<" -> PROCESS CREATOR : "
				  <<gTrack->GetCreatorProcess()->GetProcessName();
  }
#endif

  //
  //Position
  //
  const G4ThreeVector& pos = gTrack->GetPosition();
  //LogDebug("TrackerSimDebug")<<" ENERGY MeV "<<gTrack->GetKineticEnergy()<<" Energy Cut" << energyCut;
  // <<"\n TOTAL ENERGY "<<gTrack->GetTotalEnergy() <<" WEIGHT "<<gTrack->GetWeight();

  //
  // Check if in Tracker Volume
  //
  if (pos.x()*pos.x() + pos.y()*pos.y() < rTracker2 && std::abs(pos.z()) < zTracker){
    //
    // inside the Tracker
    //
    LogDebug("TrackerSimDebug")<<" INSIDE TRACKER";

    if (gTrack->GetKineticEnergy() > energyCut){
      TrackInformation* info = getTrackInformation(gTrack);
      info->storeTrack(true);
    }
    //
    // Save History?
    //
    if (gTrack->GetKineticEnergy() > energyHistoryCut){
      TrackInformation* info = getTrackInformation(gTrack);
      info->putInHistory();
      //LogDebug("TrackerSimDebug")<<" POINTER "<<info;
      // <<" track inside the tracker selected for HISTORY";
      // <<"Track ID (history track)= "<<gTrack->GetTrackID();
    }    
  }
}

void TkAccumulatingSensitiveDetector::sendHit()
{  
    if (mySimHit == nullptr) return;
    if (printHits)
    {
	TkSimHitPrinter thePrinter("TkHitPositionOSCAR.dat");
	thePrinter.startNewSimHit(GetName(),oldVolume->GetLogicalVolume()->GetName(),
				  mySimHit->detUnitId(),mySimHit->trackId(),eventno);
	thePrinter.printLocal(mySimHit->entryPoint(),mySimHit->exitPoint());
	thePrinter.printGlobal(globalEntryPoint,globalExitPoint);
	thePrinter.printHitData(mySimHit->energyLoss(),mySimHit->timeOfFlight());
	thePrinter.printMomentumOfTrack(mySimHit->pabs(),pname,
					thePrinter.getPropagationSign(globalEntryPoint,globalExitPoint));
	thePrinter.printGlobalMomentum(px,py,pz);
	LogDebug("TrackerSimDebug")<< " Storing PSimHit: " << mySimHit->detUnitId() 
				   << " " << mySimHit->trackId() << " " << mySimHit->energyLoss() 
				   << " " << mySimHit->entryPoint() << " " << mySimHit->exitPoint();
    }
    
    if (mySimHit->timeOfFlight() < theTofLimit)
	slaveLowTof->processHits(*mySimHit);  // implicit conversion (slicing) to PSimHit!!!
    else
	slaveHighTof->processHits(*mySimHit); // implicit conversion (slicing) to PSimHit!!!
    //
    // clean up
    delete mySimHit;
    mySimHit = nullptr;
    lastTrack = 0;
    lastId = 0;
}

void TkAccumulatingSensitiveDetector::createHit(const G4Step * aStep)
{
    // VI: previous hit should be already deleted 
    //     in past here was a check if a hit is inside a sensitive detector,
    //     this is not needed, because call to senstive detector happens 
    //     only inside the volume
    const G4Track * theTrack  = aStep->GetTrack(); 
    Local3DPoint theExitPoint = toOrcaRef(LocalPostStepPosition(aStep)); 
    Local3DPoint theEntryPoint;
    //
    //  Check particle type - for gamma and neutral hadrons energy deposition
    //  should be local (VI)
    //
    if(0.0 == theTrack->GetDefinition()->GetPDGCharge()) {
      theEntryPoint = theExitPoint; 
    } else {
      theEntryPoint = toOrcaRef(LocalPreStepPosition(aStep));
    }

    //
    //	This allows to send he skipEvent if it is outside!
    //
    const G4StepPoint* preStepPoint = aStep->GetPreStepPoint();
    float thePabs             = preStepPoint->GetMomentum().mag()/GeV;
    float theTof              = preStepPoint->GetGlobalTime()/nanosecond;
    float theEnergyLoss       = aStep->GetTotalEnergyDeposit()/GeV;
    int theParticleType       = myG4TrackToParticleID->particleID(theTrack);
    uint32_t theDetUnitId     = setDetUnitId(aStep);
    unsigned int theTrackID   = theTrack->GetTrackID();
    if (theDetUnitId == 0)
    {
      edm::LogError("TkAccumulatingSensitiveDetector::createHit") 
	<< " theDetUnitId is not valid for " << GetName();
      throw cms::Exception("TkAccumulatingSensitiveDetector::createHit")
	<< "cannot get theDetUnitId for G4Track " << theTrackID;
    }
  
    // To whom assign the Hit?
    // First iteration: if the track is to be stored, use the current number;
    // otherwise, get to the mother
    unsigned  int theTrackIDInsideTheSimHit=theTrackID;
    
    G4VUserTrackInformation * info = theTrack->GetUserInformation();
    if (info == nullptr) {
      edm::LogError("TkAccumulatingSensitiveDetector::createHit") 
	<< " no UserTrackInformation available for trackID= " << theTrackID;
      throw cms::Exception("TkAccumulatingSensitiveDetector::createHit")
	<< " cannot handle hits for tracking in " << GetName();
    } else {
      TrackInformation * temp = dynamic_cast<TrackInformation* >(info);
      if (temp ==nullptr) {
	edm::LogError("TkAccumulatingSensitiveDetector::createHit") 
	  << " G4VUserTrackInformation is not a TrackInformation for trackID= " 
	  << theTrackID;
	throw cms::Exception("TkAccumulatingSensitiveDetector::createHit")
	  << " cannot handle hits for tracking in " << GetName();
      } else {
	if (temp->storeTrack() == false) {
	  // Go to the mother!
	  theTrackIDInsideTheSimHit = theTrack->GetParentID();
	  LogDebug("TrackerSimDebug")
	    << " TkAccumulatingSensitiveDetector::createHit(): setting the TrackID from "
	    << theTrackIDInsideTheSimHit
	    << " to the mother one " << theTrackIDInsideTheSimHit << " " << theEnergyLoss;
	} else {
	  LogDebug("TrackerSimDebug")
	    << " TkAccumulatingSensitiveDetector:createHit(): leaving the current TrackID " 
	    << theTrackIDInsideTheSimHit;
	}
      }
    }
        
    const G4ThreeVector& gmd  = preStepPoint->GetMomentumDirection();
    // convert it to local frame
    G4ThreeVector lmd = ((G4TouchableHistory *)(preStepPoint->GetTouchable()))->GetHistory()
      ->GetTopTransform().TransformAxis(gmd);
    Local3DPoint lnmd = toOrcaRef(ConvertToLocal3DPoint(lmd));
    float theThetaAtEntry = lnmd.theta();
    float thePhiAtEntry = lnmd.phi();
    
    mySimHit = new UpdatablePSimHit(theEntryPoint,theExitPoint,thePabs,theTof,
				    theEnergyLoss,theParticleType,theDetUnitId,
				    theTrackIDInsideTheSimHit,theThetaAtEntry,thePhiAtEntry,
				    theG4ProcessTypeEnumerator->processId(theTrack->GetCreatorProcess()));  
    lastId = theDetUnitId;
    lastTrack = theTrackID;

    // only for debugging
    if (printHits) {
      globalEntryPoint = toOrcaRef(ConvertToLocal3DPoint(preStepPoint->GetPosition()));
      globalExitPoint  = toOrcaRef(ConvertToLocal3DPoint(aStep->GetPostStepPoint()->GetPosition()));
      px  = preStepPoint->GetMomentum().x()/GeV;
      py  = preStepPoint->GetMomentum().y()/GeV;
      pz  = preStepPoint->GetMomentum().z()/GeV;
      oldVolume = preStepPoint->GetPhysicalVolume();
      pname = theTrack->GetDefinition()->GetParticleName();
      LogDebug("TrackerSimDebug")<< " Created PSimHit: " << pname
				 << " " << mySimHit->detUnitId() << " " << mySimHit->trackId()
				 << " " << mySimHit->energyLoss() << " " << mySimHit->entryPoint() 
				 << " " << mySimHit->exitPoint();
    }
}

void TkAccumulatingSensitiveDetector::updateHit(const G4Step * aStep)
{
    // VI: in past here was a check if a hit is inside a sensitive detector,
    //     this is not needed, because call to senstive detector happens 
    //     only inside the volume
    Local3DPoint theExitPoint = toOrcaRef(LocalPostStepPosition(aStep)); 
    float theEnergyLoss = aStep->GetTotalEnergyDeposit()/GeV;
    mySimHit->setExitPoint(theExitPoint);
    mySimHit->addEnergyLoss(theEnergyLoss);
    if (printHits) {
      globalExitPoint = toOrcaRef(ConvertToLocal3DPoint(aStep->GetPostStepPoint()->GetPosition()));
    }
    LogDebug("TrackerSimDebug")
      << " updateHit: Eloss= " << mySimHit->energyLoss()
      << " new exitpoint of " << aStep->GetTrack()->GetDefinition()->GetParticleName() 
      << " " << theExitPoint << " deltaEloss= " << theEnergyLoss
      << "\n Updated PSimHit: " << mySimHit->detUnitId() << " " << mySimHit->trackId()
      << " " << mySimHit->energyLoss() << " " << mySimHit->entryPoint() 
      << " " << mySimHit->exitPoint();
}

bool TkAccumulatingSensitiveDetector::newHit(const G4Step * aStep)
{
    const G4Track * theTrack = aStep->GetTrack(); 

    // for neutral particles do not merge hits (V.I.) 
    if(0.0 == theTrack->GetDefinition()->GetPDGCharge()) return true;

    uint32_t theDetUnitId = setDetUnitId(aStep);
    unsigned int theTrackID = theTrack->GetTrackID();

    LogDebug("TrackerSimDebug")<< " OLD(detID,trID) = (" << lastId << "," << lastTrack 
			       << "), NEW = (" << theDetUnitId << "," << theTrackID 
			       << ") Step length(mm)= " << aStep->GetStepLength() << " return "
			       << ((theTrackID == lastTrack) && (lastId == theDetUnitId));

    return ((theTrackID == lastTrack) && (lastId == theDetUnitId) && closeHit(aStep)) 
      ? false : true;
}

bool TkAccumulatingSensitiveDetector::closeHit(const G4Step * aStep)
{
    const float tolerance2 = 2.5f-5; // (50 micron)^2 are allowed between entry and exit 
    Local3DPoint theEntryPoint = toOrcaRef(LocalPreStepPosition(aStep));  
    LogDebug("TrackerSimDebug")<< " closeHit: distance = " << (mySimHit->exitPoint()-theEntryPoint).mag(); 
    return ((mySimHit->exitPoint()-theEntryPoint).mag2() < tolerance2) ? true : false;
}

void TkAccumulatingSensitiveDetector::EndOfEvent(G4HCofThisEvent *)
{
  LogDebug("TrackerSimDebug")<< " Saving the last hit in a ROU " << GetName();
  if (mySimHit != nullptr) sendHit();
}

void TkAccumulatingSensitiveDetector::update(const BeginOfEvent * i)
{
    clearHits();
    eventno = (*i)()->GetEventID();
    delete mySimHit;
    mySimHit = nullptr;
}

void TkAccumulatingSensitiveDetector::update(const BeginOfJob * i)
{
    edm::ESHandle<GeometricDet> pDD;
    const edm::EventSetup* es = (*i)();
    es->get<IdealGeometryRecord>().get( pDD );

    edm::ESTransientHandle<DDCompactView> pView;
    es->get<IdealGeometryRecord>().get(pView);

    numberingScheme_=&(numberingScheme(*pView,*pDD));
}

void TkAccumulatingSensitiveDetector::clearHits()
{
    slaveLowTof->Initialize();
    slaveHighTof->Initialize();
}

TrackInformation* TkAccumulatingSensitiveDetector::getTrackInformation(const G4Track* gTrack){
  TrackInformation* info = nullptr;
  G4VUserTrackInformation* temp = gTrack->GetUserInformation();
  if (temp == nullptr){
    edm::LogError("TkAccumulatingSensitiveDetector::getTrackInformation") 
      <<" ERROR: no G4VUserTrackInformation available for track " 
      << gTrack->GetTrackID() << " Ekin(MeV)= " << gTrack->GetKineticEnergy()
      << "  " << gTrack->GetDefinition()->GetParticleName();
    throw cms::Exception("TkAccumulatingSensitiveDetector::getTrackInformation")
      << " cannot handle hits for tracking in " << GetName();
  }else{
    info = dynamic_cast<TrackInformation*>(temp);
    if (info == nullptr){
      edm::LogError("TkAccumulatingSensitiveDetector::getTrackInformation") 
	<< " G4VUserTrackInformation is not a TrackInformation for " 
	<<"TrackID= " << gTrack->GetTrackID() << " Ekin(MeV)= " << gTrack->GetKineticEnergy()
	<< "  " << gTrack->GetDefinition()->GetParticleName();
      throw cms::Exception("TkAccumulatingSensitiveDetector::getTrackInformation")
	<< " cannot handle hits for tracking in " << GetName();
    }
  }
  return info;
}

void TkAccumulatingSensitiveDetector::fillHits(edm::PSimHitContainer& cc, const std::string& hname){

  if (slaveLowTof->name()  == hname)      { cc=slaveLowTof->hits(); }
  else if (slaveHighTof->name() == hname) { cc=slaveHighTof->hits();}
}

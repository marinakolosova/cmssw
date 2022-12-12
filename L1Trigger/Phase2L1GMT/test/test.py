# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --processName=L1REPR --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent FEVTDEBUGHLT -s RAW2DIGI,L1 --datatier F1;95;0cEVTDEBUGHLT --geometry Extended2026D49 --fileout file:/tmp/step1_Reprocess_L1.root --no_exec --nThreads 8 --python step1_L1_Reprocess.py --filein das:/MinBias_TuneCP5_14TeV-pythia8/Phase2HLTTDRSummer20L1T-PU200_111X_mcRun4_realistic_T15_v1-v2/FEVT --customise L1Trigger/Configuration/customisePhase2.addHcalTriggerPrimitives --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('L1REPR',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff') # Needed for MuonTPS
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('L1Trigger.L1TMuonTPS.L1TTrackerPlusStubs_cfi') # Adding MuonTPS

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/0049E1A3-5419-A842-B547-C8D0614FB5DB.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/0065934B-58A7-F841-851A-C37A3213387B.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/00A87F28-CB5B-D645-8AB6-BE75DF907B84.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/01866908-2916-EC46-86F2-FB6A25C6E086.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/02D8EF31-D7A9-6347-B667-48540B8B31E7.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/03DD7C0A-2E72-1E4B-8B85-38981A788A0C.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/05408FD4-875F-A249-BCCF-17EE88510376.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/0551F50A-0551-DA4C-B231-EC3EEE56CA71.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/05CE64A3-D52D-5643-B4AF-9BD085031661.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/064A41B6-CB98-5D4B-A198-4E1129A8C332.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/065829E0-A646-2846-8A3E-372C0421C178.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/065D5634-CB70-824A-B0F9-CC5F35036411.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/06ED6505-E897-1D4B-922A-35A629A5F8BB.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/07297664-7761-6B47-9F38-DA1B15868E26.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/083CF89B-7109-6545-9C79-6ECD6B50D30F.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/08CF97DD-0618-084F-ACD0-978CC59069D2.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/08FFC260-C76C-B14D-811A-F6BED73FB6C9.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/094DF951-601C-8448-9AC7-9F73D9E6650A.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/0A421F2B-6B0E-0145-8F80-5AC46957A32A.root',
        '/store/mc/Phase2HLTTDRWinter20DIGI/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/PU200_withNewMB_110X_mcRun4_realistic_v3_ext1-v1/50000/0C17EF66-41EA-724C-9E20-8094B7384BB9.root',
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('test.root'),
    outputCommands = cms.untracked.vstring(
        "drop *_*_*_*",
        "keep *_simCscTriggerPrimitiveDigis_*_*",
        "keep *_dtTriggerPhase2PrimitiveDigis_*_*",
        "keep *_simDtTriggerPrimitiveDigis_*_*",
        "keep *_simMuonRPCDigis_*_*",
        "keep *_simMuonME0*_*_*",
        "keep *_simMuonGEMDigis*_*_*",
        "keep *_simBmtfDigis_*_*",
        "keep *_simEmtfDigis_*_*",
        "keep *_simOmtfDigis_*_*",
        "keep *_genParticles_*_*",
        "keep *_TTTracksFromTrackletEmulation_Level1TTTracks_*"
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
process.L1TrackTrigger_step = cms.Path(process.L1TrackTrigger) # Needed for MuonTPS
#process.pL1TMuonTPS = cms.Path(process.l1TrackerPlusStubsSequence) # Adding MuonTPS
process.endjob_step = cms.EndPath(process.endOfProcess)
process.e = cms.EndPath(process.out)


#Calibrate Digis
process.load("L1Trigger.DTTriggerPhase2.CalibratedDigis_cfi")
process.CalibratedDigis.dtDigiTag = "simMuonDTDigis" 
process.CalibratedDigis.scenario = 0

#DTTriggerPhase2
process.load("L1Trigger.DTTriggerPhase2.dtTriggerPhase2PrimitiveDigis_cfi")
process.dtTriggerPhase2PrimitiveDigis.debug = False
process.dtTriggerPhase2PrimitiveDigis.dump = False
process.dtTriggerPhase2PrimitiveDigis.scenario = 0


#process.schedule = cms.Schedule(process.L1TrackTrigger_step,process.pL1TMuonTPS,process.endjob_step,process.e) # Adding MuonTPS

process.stubs = cms.EDProducer("Phase2L1TGMTStubProducer",
    verbose = cms.int32(0),
    srcCSC = cms.InputTag("simCscTriggerPrimitiveDigis"),
    srcDT = cms.InputTag("dtTriggerPhase2PrimitiveDigis"),
    srcDTTheta = cms.InputTag("simDtTriggerPrimitiveDigis"),
    srcRPC = cms.InputTag("simMuonRPCDigis"),
    Endcap =cms.PSet(                            
        verbose              = cms.uint32(0),
        minBX                = cms.int32(0),                           
        maxBX                = cms.int32(0),         
        coord1LSB            = cms.double(0.00076660156*32), 
        eta1LSB              = cms.double(7.68334e-04*32), 
        coord2LSB            = cms.double(0.00076660156*32), 
        eta2LSB              = cms.double(7.68334e-04*32),
        phiMatch             = cms.double(0.05),
        etaMatch             = cms.double(0.1)
    ),
    Barrel = cms.PSet(                         
        verbose            = cms.int32(0),
        minPhiQuality      = cms.int32(0),
        minThetaQuality    = cms.int32(0),
        minBX              = cms.int32(-100),                           
        maxBX              = cms.int32(100),                           
        phiLSB             = cms.double(0.00076660156*32),
        phiBDivider        = cms.int32(1),
        etaLSB             = cms.double(7.68334e-04*32), 
        eta_1              = cms.vint32(int(-1503/32), int(-1446/32), int(-1387/32), int(-1327/32), int(-1266/32), int(-1194/32), int(-1125/32), int(-985/32), int(-916/32), int(-839/32), int(-752/32), int(-670/32), int(-582/32), int(-489/32), int(-315/32), int(-213/32), int(-115/32), int(-49/32), int(49/32), int(115/32), int(213/32), int(315/32), int(489/32), int(582/32), int(670/32), int(752/32), int(839/32), int(916/32), int(985/32), int(1125/32), int(1194/32), int(1266/32), int(1327/32), int(1387/32), int(1446/32), int(1503)),
        eta_2              = cms.vint32(int(-1334/32), int(-1279/32), int(-1227/32), int(-1168/32), int(-1109/32), int(-1044/32), int(-982/32), int(-861/32), int(-793/32), int(-720/32), int(-648/32), int(-577/32), int(-496/32), int(-425/32), int(-268/32), int(-185/32), int(-97/32), int(-51/32), int(51/32), int(97/32), int(185/32), int(268/32), int(425/32), int(496/32), int(577/32), int(648/32), int(720/32), int(793/32), int(861/32), int(982/32), int(1044/32), int(1109/32), int(1168/32), int(1227/32), int(1279/32), int(1334)),
        eta_3              = cms.vint32(int(-1148/32), int(-1110/32), int(-1051/32), int(-1004/32), int(-947/32), int(-895/32), int(-839/32), int(-728/32), int(-668/32), int(-608/32), int(-546/32), int(-485/32), int(-425/32), int(-366/32), int(-222/32), int(-155/32), int(-87/32), int(-40/32), int(40/32), int(87/32), int(155/32), int(222/32), int(366/32), int(425/32), int(485/32), int(546/32), int(608/32), int(668/32), int(728/32), int(839/32), int(895/32), int(947/32), int(1004/32), int(1051/32), int(1110/32), int(1148)),
        coarseEta_1        = cms.vint32(int(0/32), int(758/32), int(1336/32)),
        coarseEta_2        = cms.vint32(int(0/32), int(653/32), int(1168/32)),
        coarseEta_3        = cms.vint32(int(0/32), int(552/32), int(1001/32)),
        coarseEta_4        = cms.vint32(int(0/32), int(478/32), int(878/32)),
        phiOffset          = cms.vint32(int(75/32),int(-30/32), int(+26/32),int(0))    
    )
)

process.prod = cms.EDProducer('Phase2L1TGMTProducer',
                              srcTracks = cms.InputTag("TTTracksFromTrackletEmulation:Level1TTTracks"),
                              srcStubs  = cms.InputTag('stubs'),
                              srcBMTF   = cms.InputTag('simBmtfDigis','BMTF'),
                              srcEMTF   = cms.InputTag('simEmtfDigis','EMTF'),
                              srcOMTF   = cms.InputTag('simOmtfDigis','OMTF'),
                              
                              minTrackStubs = cms.int32(4),
                              
                              muonBXMin = cms.int32(0),
                              muonBXMax = cms.int32(0),
                              
                              verbose   = cms.int32(1),
                              # -------------------------- added by marina - start
                              trackConverter  = cms.PSet(
                                  verbose = cms.int32(1)
                              ),
                              roiTrackAssociator  = cms.PSet(
                                  verbose=cms.int32(1)
                              ),
                              trackMatching  = cms.PSet(
                                  verbose=cms.int32(1)
                              ),
                              isolation  = cms.PSet(
                                  AbsIsoThresholdL = cms.int32(0),
                                  AbsIsoThresholdM = cms.int32(0),
                                  AbsIsoThresholdT = cms.int32(0),
                                  RelIsoThresholdL = cms.double(0),
                                  RelIsoThresholdM = cms.double(0),
                                  RelIsoThresholdT = cms.double(0),
                                  verbose       = cms.int32(0),
                                  IsodumpForHLS = cms.int32(0),
                              ),
                              tauto3mu = cms.PSet(),
                              # ------------------------- added by marina - end
                              # are the following needed?
                              IsoThreshold1 = cms.int32(0),
                              IsoThreshold2 = cms.int32(0),
                              IsoThreshold3 = cms.int32(0),
                              IsoThreshold4 = cms.int32(0),
                              IsodumpForHLS = cms.int32(0)
                          )

process.testpath=cms.Path(process.CalibratedDigis*process.dtTriggerPhase2PrimitiveDigis*process.stubs*process.prod)
#process.testpath=cms.Path(process.CalibratedDigis*process.dtTriggerPhase2PrimitiveDigis)
process.schedule = cms.Schedule(process.L1TrackTrigger_step,process.testpath,process.endjob_step,process.e)


from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2
from L1Trigger.Configuration.customisePhase2 import addHcalTriggerPrimitives 

#call to customisation function addHcalTriggerPrimitives imported from L1Trigger.Configuration.customisePhase2
process = addHcalTriggerPrimitives(process)

# End of customisation functions

# Customisation from command line

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2TTNoMC # To make the cfg work
from L1Trigger.Configuration.customisePhase2TTNoMC import customisePhase2TTNoMC  # To make the cfg work

#call to customisation function customisePhase2TTNoMC imported from L1Trigger.Configuration.customisePhase2TTNoMC # To make the cfg work
process = customisePhase2TTNoMC(process) # To make the cfg work

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.TopMonitor_cfi import hltTOPmonitoring

eleJet_jet = hltTOPmonitoring.clone()
eleJet_jet.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/EleJet/JetMonitor')
eleJet_jet.nmuons = cms.uint32(0)
eleJet_jet.nelectrons = cms.uint32(1)
eleJet_jet.njets = cms.uint32(1)
eleJet_jet.eleSelection = cms.string('pt>50 & abs(eta)<2.1 & (dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1')
eleJet_jet.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
eleJet_jet.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.7,-1.2,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.2,1.7,2.1)
eleJet_jet.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.7,-1.2,-0.6,-0.3,0,0.3,0.6,1.2,1.7,2.1)
eleJet_jet.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
eleJet_jet.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
eleJet_jet.histoPSet.jetPtBinning = cms.vdouble(0,30,32.5,35,37.5,40,45,50,60,80,120,200,400)
eleJet_jet.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,45,50,60,80,100,200,400)
eleJet_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v*')
eleJet_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_v*',
                                                             'HLT_Ele35_WPTight_Gsf_v*',
                                                             'HLT_Ele38_WPTight_Gsf_v*',
                                                             'HLT_Ele40_WPTight_Gsf_v*',)

eleJet_ele = hltTOPmonitoring.clone()
eleJet_ele.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/EleJet/ElectronMonitor')
eleJet_ele.nmuons = cms.uint32(0)
eleJet_ele.nelectrons = cms.uint32(1)
eleJet_ele.njets = cms.uint32(1)
eleJet_ele.eleSelection = cms.string('pt>25 & abs(eta)<2.1 & (dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1')
eleJet_ele.jetSelection = cms.string('pt>50 & abs(eta)<2.4')
eleJet_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.7,-1.2,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.2,1.7,2.1)
eleJet_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.7,-1.2,-0.6,-0.3,0,0.3,0.6,1.2,1.7,2.1)
eleJet_ele.histoPSet.elePtBinning = cms.vdouble(0,25,27.5,30,32.5,35,40,45,50,60,80,120,200,400)
eleJet_ele.histoPSet.elePtBinning2D = cms.vdouble(0,25,27.5,30,35,40,50,60,80,100,200,400)
eleJet_ele.histoPSet.jetPtBinning = cms.vdouble(0,50,60,80,120,200,400)
eleJet_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,50,60,80,100,200,400)
eleJet_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v*')
eleJet_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')

eleJet_all = hltTOPmonitoring.clone()
eleJet_all.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/EleJet/GlobalMonitor')
eleJet_all.nmuons = cms.uint32(0)
eleJet_all.nelectrons = cms.uint32(1)
eleJet_all.njets = cms.uint32(1)
eleJet_all.eleSelection = cms.string('pt>25 & abs(eta)<2.1 & (dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1')
eleJet_all.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
eleJet_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.7,-1.2,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.2,1.7,2.1)
eleJet_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.7,-1.2,-0.6,-0.3,0,0.3,0.6,1.2,1.7,2.1)
eleJet_all.histoPSet.elePtBinning = cms.vdouble(0,25,27.5,30,32.5,35,40,45,50,60,80,120,200,400)
eleJet_all.histoPSet.elePtBinning2D = cms.vdouble(0,25,27.5,30,35,40,50,60,80,100,200,400)
eleJet_all.histoPSet.jetPtBinning = cms.vdouble(0,30,32.5,35,37.5,40,50,60,80,120,200,400)
eleJet_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,45,50,60,80,100,200,400)
eleJet_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v*')
# eleJet_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')


eleHT_ht = hltTOPmonitoring.clone()
eleHT_ht.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/EleHT/HTMonitor')
eleHT_ht.nmuons = cms.uint32(0)
eleHT_ht.nelectrons = cms.uint32(1)
eleHT_ht.njets = cms.uint32(2)
eleHT_ht.eleSelection = cms.string('pt>50 & abs(eta)<2.1 & (dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1')
eleHT_ht.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
eleHT_ht.HTcut = cms.double(100)
eleHT_ht.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.7,-1.2,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.2,1.7,2.1)
eleHT_ht.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.7,-1.2,-0.6,-0.3,0,0.3,0.6,1.2,1.7,2.1)
eleHT_ht.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
eleHT_ht.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
eleHT_ht.histoPSet.jetPtBinning = cms.vdouble(0,30,40,50,60,80,120,200,400)
eleHT_ht.histoPSet.jetPtBinning2D = cms.vdouble(0,30,40,60,80,100,200,400)
eleHT_ht.histoPSet.HTBinning  = cms.vdouble(0,100,120,140,150,160,175,200,300,400,500,700)
eleHT_ht.histoPSet.HTBinning2D  = cms.vdouble(0,100,125,150.175,200,400,700)
eleHT_ht.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*')
eleHT_ht.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele30_eta2p1_WPTight_Gsf_v*',
                                                           'HLT_Ele35_WPTight_Gsf_v*',
                                                           'HLT_Ele38_WPTight_Gsf_v*',
                                                           'HLT_Ele40_WPTight_Gsf_v*',)

eleHT_ele = hltTOPmonitoring.clone()
eleHT_ele.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/EleHT/ElectronMonitor')
eleHT_ele.nmuons = cms.uint32(0)
eleHT_ele.nelectrons = cms.uint32(1)
eleHT_ele.njets = cms.uint32(2)
eleHT_ele.eleSelection = cms.string('pt>25 & abs(eta)<2.1 & (dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1')
eleHT_ele.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
eleHT_ele.HTcut = cms.double(200)
eleHT_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.7,-1.2,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.2,1.7,2.1)
eleHT_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.7,-1.2,-0.6,-0.3,0,0.3,0.6,1.2,1.7,2.1)
eleHT_ele.histoPSet.elePtBinning = cms.vdouble(0,25,27.5,30,32.5,35,40,45,50,60,80,120,200,400)
eleHT_ele.histoPSet.elePtBinning2D = cms.vdouble(0,25,27.5,30,35,40,50,60,80,100,200,400)
eleHT_ele.histoPSet.jetPtBinning = cms.vdouble(0,30,40,50,60,80,120,200,400)
eleHT_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,30,40,60,80,100,200,400)
eleHT_ele.histoPSet.HTBinning  = cms.vdouble(0,200,250,300,350,400,500,700)
eleHT_ele.histoPSet.HTBinning2D  = cms.vdouble(0,200,250,300,400,500,700)
eleHT_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*')
eleHT_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_HT200_v*',
                                                            'HLT_HT275_v*',)

eleHT_all = hltTOPmonitoring.clone()
eleHT_all.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/EleHT/GlobalMonitor')
eleHT_all.nmuons = cms.uint32(0)
eleHT_all.nelectrons = cms.uint32(1)
eleHT_all.njets = cms.uint32(2)
eleHT_all.eleSelection = cms.string('pt>25 & abs(eta)<2.1 & (dr03TkSumPt+dr04EcalRecHitSumEt+dr04HcalTowerSumEt)/pt<0.1')
eleHT_all.jetSelection = cms.string('pt>30 & abs(eta)<2.4')
eleHT_all.HTcut = cms.double(100)
eleHT_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.7,-1.2,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.2,1.7,2.1)
eleHT_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.7,-1.2,-0.6,-0.3,0,0.3,0.6,1.2,1.7,2.1)
eleHT_all.histoPSet.elePtBinning = cms.vdouble(0,25,27.5,30,32.5,35,40,45,50,60,80,120,200,400)
eleHT_all.histoPSet.elePtBinning2D = cms.vdouble(0,25,27.5,30,35,40,50,60,80,100,200,400)
eleHT_all.histoPSet.jetPtBinning = cms.vdouble(0,30,40,50,60,80,120,200,400)
eleHT_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,40,60,80,100,200,400)
eleHT_all.histoPSet.HTBinning  = cms.vdouble(0,100,120,140,150,160,175,200,300,400,500,700)
eleHT_all.histoPSet.HTBinning2D  = cms.vdouble(0,100,125,150.175,200,400,700)
eleHT_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*')
# eleHT_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')


#ATHER
topSingleMuonHLTValidation = hltTOPmonitoring.clone()
topSingleMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/SingleLepton/SingleMuon/')
topSingleMuonHLTValidation.nmuons = cms.uint32(1)
topSingleMuonHLTValidation.nelectrons = cms.uint32(0)
topSingleMuonHLTValidation.njets = cms.uint32(4)
topSingleMuonHLTValidation.eleSelection = cms.string('pt>30 & abs(eta)<2.5 & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')
topSingleMuonHLTValidation.muoSelection = cms.string('pt>26 & abs(eta)<2.1 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')
topSingleMuonHLTValidation.jetSelection = cms.string('pt>20 & abs(eta)<2.5')
topSingleMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu20_v*', 'HLT_TkMu20_v*' , 'HLT_Mu27_v*', 'HLT_TkMu27_v*', 'HLT_TkMu50_v*', 'HLT_Mu50_v*', 'HLT_IsoMu24_eta2p1_v*', 'HLT_IsoMu24_v*', 'HLT_IsoMu27_v*', 'HLT_IsoMu20_v*', 'HLT_IsoTkMu24_eta2p1_v*', 'HLT_IsoTkMu24_v*', 'HLT_IsoTkMu27_v*', 'HLT_IsoTkMu20_v*'])



topDiElectronHLTValidation = hltTOPmonitoring.clone()
topDiElectronHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/DiLepton/DiElectron/')
topDiElectronHLTValidation.nmuons = cms.uint32(0)
topDiElectronHLTValidation.nelectrons = cms.uint32(2)
topDiElectronHLTValidation.njets = cms.uint32(2)
topDiElectronHLTValidation.eleSelection = cms.string('pt>20 & abs(eta)<2.5  & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')
topDiElectronHLTValidation.muoSelection = cms.string('pt>20 & abs(eta)<2.4 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')   
topDiElectronHLTValidation.jetSelection = cms.string('pt>30 & abs(eta)<2.5')
topDiElectronHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Ele12_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*'])



topDiMuonHLTValidation = hltTOPmonitoring.clone()
topDiMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/DiLepton/DiMuon/')
topDiMuonHLTValidation.nmuons = cms.uint32(2)
topDiMuonHLTValidation.nelectrons = cms.uint32(0)
topDiMuonHLTValidation.njets = cms.uint32(2)
topDiMuonHLTValidation.eleSelection = cms.string('pt>20 & abs(eta)<2.5  & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')              
topDiMuonHLTValidation.muoSelection = cms.string('pt>20 & abs(eta)<2.4 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')  
topDiMuonHLTValidation.jetSelection = cms.string('pt>30 & abs(eta)<2.5')
topDiMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*','HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*'])



topElecMuonHLTValidation = hltTOPmonitoring.clone()
topElecMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/Top/DiLepton/ElecMuon/')
topElecMuonHLTValidation.nmuons = cms.uint32(1)
topElecMuonHLTValidation.nelectrons = cms.uint32(1)
topElecMuonHLTValidation.njets = cms.uint32(2)
topElecMuonHLTValidation.eleSelection = cms.string('pt>20 & abs(eta)<2.5 & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')
topElecMuonHLTValidation.muoSelection = cms.string('pt>20 & abs(eta)<2.4 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')           
topElecMuonHLTValidation.jetSelection = cms.string('pt>30 & abs(eta)<2.5')
topElecMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*','HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*'])



singleTopSingleMuonHLTValidation = hltTOPmonitoring.clone()
singleTopSingleMuonHLTValidation.FolderName = cms.string('HLT/TopHLTOffline/TopMonitor/SingleTop/SingleMuon/')
singleTopSingleMuonHLTValidation.nmuons = cms.uint32(1)
singleTopSingleMuonHLTValidation.nelectrons = cms.uint32(0)
singleTopSingleMuonHLTValidation.njets = cms.uint32(2)
singleTopSingleMuonHLTValidation.eleSelection = cms.string('pt>30 & abs(eta)<2.5 & (dr03TkSumPt+dr03EcalRecHitSumEt+dr03HcalTowerSumEt)/pt < 0.1')   
singleTopSingleMuonHLTValidation.muoSelection = cms.string('pt>26 & abs(eta)<2.1 & (pfIsolationR04.sumChargedHadronPt+pfIsolationR04.sumPhotonEt+pfIsolationR04.sumNeutralHadronEt)/pt < 0.12')
singleTopSingleMuonHLTValidation.jetSelection = cms.string('pt>40 & abs(eta)<5.0')
singleTopSingleMuonHLTValidation.numGenericTriggerEventPSet.hltPaths = cms.vstring(['HLT_Mu20_v*', 'HLT_TkMu20_v*' , 'HLT_Mu27_v*', 'HLT_TkMu27_v*', 'HLT_TkMu50_v*', 'HLT_Mu50_v*', 'HLT_IsoMu24_eta2p1_v*', 'HLT_IsoMu24_v*', 'HLT_IsoMu27_v*', 'HLT_IsoMu20_v*', 'HLT_IsoTkMu24_eta2p1_v*', 'HLT_IsoTkMu24_v*', 'HLT_IsoTkMu27_v*', 'HLT_IsoTkMu20_v*'])


# Marina
fullyhadronic_DoubleBTag_all = hltTOPmonitoring.clone()
fullyhadronic_DoubleBTag_all.FolderName   = cms.string('HLT/TopHLTOffline/TopMonitor/FullyHadronic/DoubleBTag/GlobalMonitor/')
# Selections
fullyhadronic_DoubleBTag_all.leptJetDeltaRmin = cms.double(0.0)
fullyhadronic_DoubleBTag_all.njets            = cms.uint32(6)
fullyhadronic_DoubleBTag_all.jetSelection     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_DoubleBTag_all.HTdefinition     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_DoubleBTag_all.HTcut            = cms.double(450)
fullyhadronic_DoubleBTag_all.nbjets           = cms.uint32(2)
fullyhadronic_DoubleBTag_all.bjetPtCut        = cms.double(30)
fullyhadronic_DoubleBTag_all.bjetAbsEtaCut    = cms.double(2.4)
fullyhadronic_DoubleBTag_all.workingpoint     = cms.double(0.8484) # Medium
# Binning
fullyhadronic_DoubleBTag_all.histoPSet.htPSet = cms.PSet(nbins=cms.int32(50), xmin=cms.double(0.0), xmax=cms.double(1000) )
fullyhadronic_DoubleBTag_all.histoPSet.jetPtBinning = cms.vdouble(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,100,120,200,400)
fullyhadronic_DoubleBTag_all.histoPSet.HTBinning    = cms.vdouble(0,420,440,460,480,500,520,540,560,580,600,650,700,750,800,850,900)
# Triggers 
fullyhadronic_DoubleBTag_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT380_SixJet32_DoubleBTagCSV_p075_v')
fullyhadronic_DoubleBTag_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu27_v')

fullyhadronic_DoubleBTag_jet = hltTOPmonitoring.clone()
fullyhadronic_DoubleBTag_jet.FolderName   = cms.string('HLT/TopHLTOffline/TopMonitor/FullyHadronic/DoubleBTag/JetMonitor/')
# Selections
fullyhadronic_DoubleBTag_jet.leptJetDeltaRmin = cms.double(0.0)
fullyhadronic_DoubleBTag_jet.njets            = cms.uint32(6)
fullyhadronic_DoubleBTag_jet.jetSelection     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_DoubleBTag_jet.HTdefinition     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_DoubleBTag_jet.HTcut            = cms.double(450)
fullyhadronic_DoubleBTag_jet.nbjets           = cms.uint32(2)
fullyhadronic_DoubleBTag_jet.bjetPtCut        = cms.double(30)
fullyhadronic_DoubleBTag_jet.bjetAbsEtaCut    = cms.double(2.4)
fullyhadronic_DoubleBTag_jet.workingpoint = cms.double(0.8484) # Medium
# Binning 
fullyhadronic_DoubleBTag_jet.histoPSet.htPSet = cms.PSet(nbins=cms.int32(50), xmin=cms.double(0.0), xmax=cms.double(1000) )
fullyhadronic_DoubleBTag_jet.histoPSet.jetPtBinning = cms.vdouble(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,100,120,200,400)
fullyhadronic_DoubleBTag_jet.histoPSet.HTBinning    = cms.vdouble(0,420,440,460,480,500,520,540,560,580,600,650,700,750,800,850,900)
# Triggers
fullyhadronic_DoubleBTag_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT380_SixJet32_DoubleBTagCSV_p075_v')
fullyhadronic_DoubleBTag_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT370_v')

fullyhadronic_DoubleBTag_bjet = hltTOPmonitoring.clone()
fullyhadronic_DoubleBTag_bjet.FolderName   = cms.string('HLT/TopHLTOffline/TopMonitor/FullyHadronic/DoubleBTag/BJetMonitor/')
# Selections
fullyhadronic_DoubleBTag_bjet.leptJetDeltaRmin = cms.double(0.0)
fullyhadronic_DoubleBTag_bjet.njets            = cms.uint32(6)
fullyhadronic_DoubleBTag_bjet.jetSelection     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_DoubleBTag_bjet.HTdefinition     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_DoubleBTag_bjet.HTcut            = cms.double(450)
fullyhadronic_DoubleBTag_bjet.nbjets           = cms.uint32(2)
fullyhadronic_DoubleBTag_bjet.bjetPtCut        = cms.double(30)
fullyhadronic_DoubleBTag_bjet.bjetAbsEtaCut    = cms.double(2.4)
fullyhadronic_DoubleBTag_bjet.workingpoint     = cms.double(0.70)
# Binning
fullyhadronic_DoubleBTag_bjet.histoPSet.htPSet = cms.PSet(nbins=cms.int32(50), xmin=cms.double(0.0), xmax=cms.double(1000) )
fullyhadronic_DoubleBTag_bjet.histoPSet.jetPtBinning = cms.vdouble(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,100,120,200,400)
fullyhadronic_DoubleBTag_bjet.histoPSet.HTBinning    = cms.vdouble(0,420,440,460,480,500,520,540,560,580,600,650,700,750,800,850,900)
# Triggers
fullyhadronic_DoubleBTag_bjet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT380_SixJet32_DoubleBTagCSV_p075_v')
fullyhadronic_DoubleBTag_bjet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT380_SixJet32_v')


fullyhadronic_SingleBTag_all = hltTOPmonitoring.clone()
fullyhadronic_SingleBTag_all.FolderName= cms.string('HLT/TopHLTOffline/TopMonitor/FullyHadronic/SingleBTag/GlobalMonitor/')
# Selections
fullyhadronic_SingleBTag_all.leptJetDeltaRmin = cms.double(0.0)
fullyhadronic_SingleBTag_all.njets            = cms.uint32(6)
fullyhadronic_SingleBTag_all.jetSelection     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_SingleBTag_all.HTdefinition     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_SingleBTag_all.HTcut            = cms.double(450)
fullyhadronic_SingleBTag_all.nbjets           = cms.uint32(2)
fullyhadronic_SingleBTag_all.bjetPtCut        = cms.double(30)
fullyhadronic_SingleBTag_all.bjetAbsEtaCut    = cms.double(2.4)
fullyhadronic_SingleBTag_all.workingpoint     = cms.double(0.8484) # Medium
# Binning
fullyhadronic_SingleBTag_all.histoPSet.htPSet = cms.PSet(nbins=cms.int32(50), xmin=cms.double(0.0), xmax=cms.double(1000) )
fullyhadronic_SingleBTag_all.histoPSet.jetPtBinning = cms.vdouble(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,100,120,200,400)
fullyhadronic_SingleBTag_all.histoPSet.HTBinning    = cms.vdouble(0,420,440,460,480,500,520,540,560,580,600,650,700,750,800,850,900)
# Triggers
fullyhadronic_SingleBTag_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT430_SixJet40_BTagCSV_p080_v')
fullyhadronic_SingleBTag_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu27_v')

fullyhadronic_SingleBTag_jet = hltTOPmonitoring.clone()
fullyhadronic_SingleBTag_jet.FolderName= cms.string('HLT/TopHLTOffline/TopMonitor/FullyHadronic/SingleBTag/JetMonitor/')
# Selection
fullyhadronic_SingleBTag_jet.leptJetDeltaRmin = cms.double(0.0)
fullyhadronic_SingleBTag_jet.njets            = cms.uint32(6)
fullyhadronic_SingleBTag_jet.jetSelection     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_SingleBTag_jet.HTdefinition     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_SingleBTag_jet.HTcut            = cms.double(450)
fullyhadronic_SingleBTag_jet.nbjets           = cms.uint32(2)
fullyhadronic_SingleBTag_jet.bjetPtCut        = cms.double(30)
fullyhadronic_SingleBTag_jet.bjetAbsEtaCut    = cms.double(2.4)
fullyhadronic_SingleBTag_jet.workingpoint     = cms.double(0.8484) # Medium
# Binning
fullyhadronic_SingleBTag_jet.histoPSet.htPSet = cms.PSet(nbins=cms.int32(50), xmin=cms.double(0.0), xmax=cms.double(1000) )
fullyhadronic_SingleBTag_jet.histoPSet.jetPtBinning = cms.vdouble(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,100,120,200,400)
fullyhadronic_SingleBTag_jet.histoPSet.HTBinning    = cms.vdouble(0,420,440,460,480,500,520,540,560,580,600,650,700,750,800,850,900)
# Triggers
fullyhadronic_SingleBTag_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT430_SixJet40_BTagCSV_p080_v')
fullyhadronic_SingleBTag_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT430_v')

fullyhadronic_SingleBTag_bjet = hltTOPmonitoring.clone()
fullyhadronic_SingleBTag_bjet.FolderName= cms.string('HLT/TopHLTOffline/TopMonitor/FullyHadronic/SingleBTag/BJetMonitor/')
# Selection
fullyhadronic_SingleBTag_bjet.leptJetDeltaRmin = cms.double(0.0)
fullyhadronic_SingleBTag_bjet.njets            = cms.uint32(6)
fullyhadronic_SingleBTag_bjet.jetSelection     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_SingleBTag_bjet.HTdefinition     = cms.string('pt>30 & abs(eta)<2.4')
fullyhadronic_SingleBTag_bjet.HTcut            = cms.double(450)
fullyhadronic_SingleBTag_bjet.nbjets           = cms.uint32(2)
fullyhadronic_SingleBTag_bjet.bjetPtCut        = cms.double(30)
fullyhadronic_SingleBTag_bjet.bjetAbsEtaCut    = cms.double(2.4)
fullyhadronic_SingleBTag_bjet.workingpoint     = cms.double(0.70)
# Binning
fullyhadronic_SingleBTag_bjet.histoPSet.htPSet = cms.PSet(nbins=cms.int32(50), xmin=cms.double(0.0), xmax=cms.double(1000) )
fullyhadronic_SingleBTag_bjet.histoPSet.jetPtBinning = cms.vdouble(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,100,120,200,400)
fullyhadronic_SingleBTag_bjet.histoPSet.HTBinning    = cms.vdouble(0,420,440,460,480,500,520,540,560,580,600,650,700,750,800,850,900)
# Triggers
fullyhadronic_SingleBTag_bjet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT430_SixJet40_BTagCSV_p080_v')
fullyhadronic_SingleBTag_bjet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFHT430_SixJet40_v')



topMonitorHLT = cms.Sequence(
    eleJet_ele
    + eleJet_jet
    + eleJet_all
    + eleHT_ele
    + eleHT_ht
    + eleHT_all
    + topSingleMuonHLTValidation
    + topDiElectronHLTValidation
    + topDiMuonHLTValidation
    + topElecMuonHLTValidation
    + singleTopSingleMuonHLTValidation
    + fullyhadronic_DoubleBTag_all
    + fullyhadronic_DoubleBTag_jet
    + fullyhadronic_DoubleBTag_bjet
    + fullyhadronic_SingleBTag_all
    + fullyhadronic_SingleBTag_jet
    + fullyhadronic_SingleBTag_bjet
    
    )

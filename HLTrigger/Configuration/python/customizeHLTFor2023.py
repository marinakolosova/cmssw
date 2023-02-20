from HLTrigger.Configuration.common import *
import FWCore.ParameterSet.Config as cms

HCAL_PFclusters_2023=[0.6,0.5,0.5,0.5]
HCAL_PFrechits_2023=[0.4,0.3,0.3,0.3]

HCAL_PFclusters_2022=[0.125, 0.25, 0.35, 0.35]
HCAL_PFrechits_2022=[0.1, 0.2, 0.3, 0.3]

def customizeHCALFor2023(process):
    return customizeHCAL(process, HCAL_PFclusters_2023, HCAL_PFrechits_2023)

def customizeHCALFor2022(process):
    return customizeHCAL(process, HCAL_PFclusters_2022, HCAL_PFrechits_2022)

def customizeHCAL(process, HCAL_PFclusters, HCAL_PFrechits):
    if hasattr(process, "hltParticleFlowClusterHBHE"):
        process.hltParticleFlowClusterHBHE.seedFinder.thresholdsByDetector[0].seedingThreshold=HCAL_PFclusters
        process.hltParticleFlowClusterHBHE.initialClusteringStep.thresholdsByDetector[0].gatheringThreshold=HCAL_PFrechits
        process.hltParticleFlowClusterHBHE.pfClusterBuilder.recHitEnergyNorms[0].recHitEnergyNorm=HCAL_PFrechits
        process.hltParticleFlowClusterHBHE.pfClusterBuilder.positionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=HCAL_PFrechits
        process.hltParticleFlowClusterHBHE.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=HCAL_PFrechits
    if hasattr(process, "hltParticleFlowClusterHCAL"):
        process.hltParticleFlowClusterHCAL.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=HCAL_PFrechits
    if hasattr(process, "hltParticleFlowRecHitHBHE"):
        process.hltParticleFlowRecHitHBHE.producers[0].qualityTests[0].cuts[0].threshold=HCAL_PFrechits

    if hasattr(process, "hltEgammaHoverE"):
        process.hltEgammaHoverE.eThresHB=HCAL_PFrechits
    if hasattr(process, "hltEgammaHoverEUnseeded"):
        process.hltEgammaHoverEUnseeded.eThresHB=HCAL_PFrechits
    if hasattr(process, "hltEgammaHToverET"):
        process.hltEgammaHToverET.eThresHB=HCAL_PFrechits
    if hasattr(process, "hltFixedGridRhoFastjetECALMFForMuons"):
        process.hltFixedGridRhoFastjetECALMFForMuons.eThresHB=HCAL_PFrechits
    if hasattr(process, "hltFixedGridRhoFastjetAllCaloForMuons"):
        process.hltFixedGridRhoFastjetAllCaloForMuons.eThresHB=HCAL_PFrechits
    if hasattr(process, "hltFixedGridRhoFastjetHCAL"):
        process.hltFixedGridRhoFastjetHCAL.eThresHB=HCAL_PFrechits

    if hasattr(process, "hltParticleFlowClusterHBHECPUOnly"):
        process.hltParticleFlowClusterHBHECPUOnly.seedFinder.thresholdsByDetector[0].seedingThreshold=HCAL_PFclusters
        process.hltParticleFlowClusterHBHECPUOnly.initialClusteringStep.thresholdsByDetector[0].gatheringThreshold=HCAL_PFrechits
        process.hltParticleFlowClusterHBHECPUOnly.pfClusterBuilder.recHitEnergyNorms[0].recHitEnergyNorm=HCAL_PFrechits
        process.hltParticleFlowClusterHBHECPUOnly.pfClusterBuilder.positionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=HCAL_PFrechits
        process.hltParticleFlowClusterHBHECPUOnly.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=HCAL_PFrechits
    if hasattr(process, "hltParticleFlowClusterHCALCPUOnly"):
        process.hltParticleFlowClusterHCALCPUOnly.pfClusterBuilder.allCellsPositionCalc.logWeightDenominatorByDetector[0].logWeightDenominator=HCAL_PFrechits
    if hasattr(process, "hltParticleFlowRecHitHBHECPUOnly"):
        process.hltParticleFlowRecHitHBHECPUOnly.producers[0].qualityTests[0].cuts[0].threshold=HCAL_PFrechits
    
    return process

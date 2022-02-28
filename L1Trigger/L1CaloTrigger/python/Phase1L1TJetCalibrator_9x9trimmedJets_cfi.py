import FWCore.ParameterSet.Config as cms
calibration = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(0.435),
        etaMin = cms.double(0),
        l1tCalibrationFactors = cms.vdouble(
            1.26806262588, 1.26806262588, 1.26806262588, 1.21946518166, 1.16379314256, 
            1.12254571737, 1.09470447579, 1.0841543755, 1.0506829785, 1.04497069514, 
            1.03934326232, 1.03345095744, 1.02750216269, 1.02112447625, 1.01574388754, 
            1.00810805817, 0.99605714473, 0.998607125466, 0.993219133111, 0.985092796485, 
            0.978878065815, 0.970789716092, 0.961656436256, 0.959516385399, 0.948147862573, 
            0.947200388265, 0.946753222399, 0.932749319061, 0.926825446704, 0.923647034369, 
            0.913806018949, 0.881718922491
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 16.6077877711, 23.758945127, 32.4028984708, 42.0487682803, 
            52.0149801449, 62.3890828336, 72.8126081905, 83.1366634984, 93.6055295245, 
            103.912979585, 114.384063612, 125.147255659, 136.35164449, 147.039551665, 
            158.871071713, 176.765709913, 197.959631424, 225.348244676, 268.360888373, 
            314.00482813, 359.527865313, 414.339896094, 450.220016892, 493.214342949, 
            532.413003663, 536.851785714, 582.845833333, 646.270833333, 675.241071429, 
            716.678571429, 850.125, float('inf')
        )
    ), 
    cms.PSet(
        etaMax = cms.double(0.783),
        etaMin = cms.double(0.435),
        l1tCalibrationFactors = cms.vdouble(
            1.27022476075, 1.27022476075, 1.27022476075, 1.23193977019, 1.17930700881, 
            1.13682836123, 1.10620197739, 1.08803729104, 1.06551671995, 1.05815998513, 
            1.05091777833, 1.04351195843, 1.03840402395, 1.02970511677, 1.02322448674, 
            1.01173641061, 0.998762625873, 1.01162336339, 1.01141830879, 1.01110184225, 
            1.01084507077, 1.01048193189, 1.01025026917, 1.00998987557, 1.00977460446, 
            1.00958480149, 1.00938402751, 1.00923173234, 1.00896205922, 1.00877952325, 
            1.00848454553, 1.00809094748
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 16.455812263, 23.4058211563, 31.8076589224, 41.2694704832, 
            51.4874752049, 61.8853021467, 72.1485970296, 82.3017709389, 92.821899346, 
            103.57630449, 114.366868474, 123.585206897, 133.756106455, 144.938211106, 
            158.174975175, 176.194963818, 195.029478711, 220.750032768, 262.570643701, 
            308.538413528, 358.248823119, 405.945769577, 445.403605016, 483.547003284, 
            516.029761905, 547.35, 575.6625, 609.5, 645.7625, 
            684.054166667, 739.270833333, float('inf')
        )
    ), 
    cms.PSet(
        etaMax = cms.double(1.131),
        etaMin = cms.double(0.783),
        l1tCalibrationFactors = cms.vdouble(
            1.26940863552, 1.26940863552, 1.26940863552, 1.21850042272, 1.16014066757, 
            1.11360382831, 1.08451810312, 1.06753212736, 1.05501857105, 1.04712872618, 
            1.03953145463, 1.03129558228, 1.02392940863, 1.01647040511, 1.00765667693, 
            0.997452910609, 0.981686885508, 0.989286565044, 0.992427119505, 0.996927682694, 
            1.00148185029, 1.00626281233, 1.01118610536, 1.01492397525, 1.0197730491, 
            1.02294548929, 1.02309909545, 1.03179752273, 1.04335891364, 1.04679419517, 
            1.04697871887, 1.05665639769
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 16.658158537, 23.8634314296, 32.6191125159, 42.4492040271, 
            52.9120745879, 63.2335833679, 73.7409226942, 84.0418964903, 94.148332101, 
            104.682994045, 115.453031153, 126.065870612, 136.150267568, 147.219321527, 
            160.155420808, 177.820618512, 198.152518248, 224.425247256, 264.972493816, 
            313.021014808, 362.557459677, 414.052651985, 460.012722795, 505.578952902, 
            548.144755747, 565.794270833, 612.7671875, 720.275, 799.854166667, 
            819.0625, 871.395833333, float('inf')
        )
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(1.131),
        l1tCalibrationFactors = cms.vdouble(
            1.35067406191, 1.35067406191, 1.35067406191, 1.29728973727, 1.23323857604, 
            1.1805316629, 1.14192838643, 1.12335733217, 1.1065907126, 1.1005436618, 
            1.09369739262, 1.08689105877, 1.08047792193, 1.07301990489, 1.06799861036, 
            1.0578434328, 1.04620517219, 1.03279280198, 1.03276766643, 1.05490363283, 
            1.0613631336, 1.07151789312, 1.0923432672, 1.10236162162, 1.12458041647, 
            1.13080591424, 1.15738278091, 1.18032588359, 1.20641120054, 1.24407887972, 
            1.35400575741
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 16.5873975086, 23.8386796597, 32.2204904018, 41.0711979739, 
            50.5775158961, 60.7008778657, 70.3592246275, 80.5033152458, 90.7596180755, 
            100.458044915, 110.727608677, 120.671367886, 131.105326809, 140.492334228, 
            151.908160762, 168.301305891, 187.144529404, 214.024926059, 257.981265415, 
            293.073033708, 313.461711712, 351.47989353, 389.330681818, 428.891447368, 
            463.797697368, 504.052083333, 564.821969697, 624.988636364, 703.225, 
            884.35, float('inf')
        )
    ), 
    cms.PSet(
        etaMax = cms.double(1.83),
        etaMin = cms.double(1.479),
        l1tCalibrationFactors = cms.vdouble(
            1.63343989323, 1.63343989323, 1.63343989323, 1.63343989323, 1.61237327031, 
            1.58129290649, 1.54880181313, 1.51437276367, 1.47566044577, 1.4333612461, 
            1.43007616674, 1.41838888661, 1.41120688977, 1.40292719871, 1.39289499293, 
            1.38154733635, 1.36518171857, 1.34179569075, 1.31131037345, 1.21512470624, 
            1.19652546359, 1.18052243169, 1.14219697689, 1.12090132667, 1.10494445955, 
            1.08116744865, 1.04972485653, 1.02388122645, 1.02106332779, 0.93821710715, 
            0.932912827317, 0.900954541324
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 14.0304333699, 19.2702852281, 25.0387598316, 31.5205165869, 
            38.5596312994, 45.8035002303, 53.2357524128, 61.14689424, 69.6758091231, 
            77.1332356297, 85.7578326385, 94.7364478681, 102.093621468, 110.807017112, 
            120.98025046, 134.167127072, 153.082251962, 178.715988762, 222.463142692, 
            269.236689617, 301.854005866, 353.065940767, 409.266883117, 444.382411067, 
            481.836956522, 533.888888889, 587.888888889, 614.90625, 695.65625, 
            778.75, 813.875, float('inf')
        )
    ), 
    cms.PSet(
        etaMax = cms.double(2.172),
        etaMin = cms.double(1.83),
        l1tCalibrationFactors = cms.vdouble(
            1.4878363144, 1.4878363144, 1.4878363144, 1.48518474866, 1.44553707599, 
            1.40800746363, 1.37269392814, 1.34268728519, 1.31155107185, 1.29724964634, 
            1.26824717982, 1.25895653021, 1.25080118853, 1.24412237598, 1.23242162986, 
            1.21983464552, 1.19947769179, 1.17915682723, 1.19591426516, 1.16520900199, 
            1.11521954951, 1.08960480689, 1.06320579474, 0.984904677633, 0.936138290441, 
            0.933930169885, 0.906741381816, 0.83587888946
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 14.6323212201, 20.2961463384, 26.9638979746, 34.2907286866, 
            42.0772600421, 50.2694398412, 58.5750993499, 67.719467579, 75.5350197454, 
            83.5378418246, 93.3456200252, 101.928069729, 109.225642018, 118.267354545, 
            130.215556381, 146.422127101, 166.433333333, 193.380670156, 231.798066137, 
            288.213675743, 341.070380435, 377.434442935, 450.6328125, 539.46875, 
            575.10625, 595.658333333, 664.208333333, float('inf')
        )
    ), 
    cms.PSet(
        etaMax = cms.double(2.5),
        etaMin = cms.double(2.172),
        l1tCalibrationFactors = cms.vdouble(
            1.34807839515, 1.34807839515, 1.34807839515, 1.33809647408, 1.28296668109, 
            1.24225927144, 1.21974923257, 1.21649951103, 1.23064762664, 1.1629973435, 
            1.15852840915, 1.15372227709, 1.15041260925, 1.14530829511, 1.13990768956, 
            1.13512676324, 1.125588949, 1.11458405118, 1.09607958404, 1.05737289774, 
            1.01895994641, 0.992663655394, 0.955621083551, 0.93513823446, 0.901760000269, 
            0.843868420876, 0.795304246419, 0.770482557252
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 15.2387099279, 20.6150961319, 27.4619155051, 35.7501165961, 
            44.8270237134, 54.3715537124, 63.4511614119, 72.3586695675, 81.6352356283, 
            91.1311643255, 101.316594704, 110.228974539, 119.468803554, 131.004799458, 
            142.185666464, 157.90981642, 180.468831547, 207.538452813, 253.905743927, 
            316.433023873, 368.898168103, 420.252232143, 466.892857143, 510.5625, 
            584.5625, 670.875, 730.375, float('inf')
        )
    ), 
    cms.PSet(
        etaMax = cms.double(5.191),
        etaMin = cms.double(3),
        l1tCalibrationFactors = cms.vdouble(
            1.0, 1.0, 1.0, 1.0, 1.0, 
            1.0, 1.0
        ),
        l1tPtBins = cms.vdouble(
            -float('inf'), 50.6626115353, 87.3285137419, 126.832659901, 178.631354515, 
            238.634615385, 218.625, float('inf')
        )
    )
)

Phase1L1TJetCalibrator = cms.EDProducer('Phase1L1TJetCalibrator',
  inputCollectionTag = cms.InputTag("Phase1L1TJetProducer", "UncalibratedPhase1L1TJetFromPfCandidates", ""),
  absEtaBinning = cms.vdouble([p.etaMin.value() for p in calibration] + [calibration[-1].etaMax.value()]),
  calibration = calibration,
  outputCollectionName = cms.string("Phase1L1TJetFromPfCandidates")
)
from collections import OrderedDict
# from coffea import hist

# process = hist.Cat("process", "Process", sorting="placement")
# process_cat = "dataset"
process_map = OrderedDict()

process_map["zll"] = [
    "DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8",
    "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8",
    "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8",
    "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8",
    "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8",
    "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8",
    "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8",
    "DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8",
    "DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8",
    "DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8",
    "DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8",
    "DYJetsToLL_Pt-50To100",
    "DYJetsToLL_Pt-100To250",
    "DYJetsToLL_Pt-250To400",
    "DYJetsToLL_Pt-400To650",
    "DYJetsToLL_Pt-650ToInf",
]
process_map["zee"] = [
    "DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zee",
    "DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zee",
    "DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zee",
    "DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zee",
    "DYJetsToLL_Pt-50To100_Zee",
    "DYJetsToLL_Pt-100To250_Zee",
    "DYJetsToLL_Pt-250To400_Zee",
    "DYJetsToLL_Pt-400To650_Zee",
    "DYJetsToLL_Pt-650ToInf_Zee",
]
process_map["zem"] = [
    "DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zem",
    "DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zem",
    "DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zem",
    "DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zem",
    "DYJetsToLL_Pt-50To100_Zem",
    "DYJetsToLL_Pt-100To250_Zem",
    "DYJetsToLL_Pt-250To400_Zem",
    "DYJetsToLL_Pt-400To650_Zem",
    "DYJetsToLL_Pt-650ToInf_Zem",
]
process_map["zmm"] = [
    "DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zmm",
    "DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zmm",
    "DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zmm",
    "DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8_Zmm",
    "DYJetsToLL_Pt-50To100_Zmm",
    "DYJetsToLL_Pt-100To250_Zmm",
    "DYJetsToLL_Pt-250To400_Zmm",
    "DYJetsToLL_Pt-400To650_Zmm",
    "DYJetsToLL_Pt-650ToInf_Zmm",
]
process_map["ztt"] = [
    "DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8_Ztt",
    "DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8_Ztt",
    "DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8_Ztt",
    "DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8_Ztt",
    "DYJetsToLL_Pt-50To100_Ztt",
    "DYJetsToLL_Pt-100To250_Ztt",
    "DYJetsToLL_Pt-250To400_Ztt",
    "DYJetsToLL_Pt-400To650_Ztt",
    "DYJetsToLL_Pt-650ToInf_Ztt",
]
# process_map["zll-ht100to200"] = [
#    'DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
# process_map["zll-ht1200to2500"] = [
#    'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
# process_map["zll-ht200to400"] = [
#    'DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
# process_map["zll-ht2500toinf"] = [
#    'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
# process_map["zll-ht400to600"] = [
#    'DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
# process_map["zll-ht600to800"] = [
#    'DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
# process_map["zll-ht800to1200"] = [
#    'DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
process_map["wjets"] = [
    "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",
    "boostedTau_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToLNu_HT-100To200",
    "WJetsToLNu_HT-1200To2500",
    "WJetsToLNu_HT-800To1200",
    "WJetsToLNu_HT-600To800",
    "WJetsToLNu_HT-2500ToInf",
    "WJetsToLNu_HT-200To400",
    "WJetsToLNu_HT-70To100",
    "WJetsToLNu_HT-400To600",
]
# process_map["wqq"] = [
#    'WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8',
#    'WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8',
#    'WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
# process_map["zqq"] = [
#    'ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8',
#    'ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8',
#    'ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8',
# ]
process_map["vqq"] = [
    "WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8",
    "WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8",
    "ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8",
    "ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8",
    "ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8",
    "ZJetsToQQ_HT-400to600",
    "ZJetsToQQ_HT-800toInf",
    "ZJetsToQQ_HT-600to800",
    "WJetsToQQ_HT-600to800",
    "WJetsToQQ_HT-800toInf",
    "WJetsToQQ_HT-400to600",
]
process_map["qcd"] = [
    "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8",
    #'QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8',
    "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8",
    "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8",
    "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8",
    "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8",
    #'QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8',
    "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8",
    "QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8",
    "QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8",
    "QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8",
    "QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8",
    "QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8",
    "boostedTau_QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8",
    "QCD_Pt_3200toInf",
    "QCD_Pt_1400to1800",
    "QCD_Pt_170to300",
    "QCD_Pt_300to470",
    "QCD_Pt_470to600",
    "QCD_Pt_1000to1400",
    "QCD_Pt_2400to3200",
    "QCD_Pt_600to800",
    "QCD_Pt_800to1000",
    "QCD_Pt_1800to2400",
]
process_map["tt-dilep"] = [
    "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8",
    "TTTo2L2Nu",
]
process_map["tt-semilep"] = [
    "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
    "TTToSemiLeptonic",
]
process_map["tt-had"] = [
    "TTToHadronic_TuneCP5_13TeV-powheg-pythia8",
    "TTToHadronic",
]
# process_map["tt"] = [
#    'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
#    'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',
#    'TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
# ]
process_map["st"] = [
    "ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8",
    "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8",
    "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8",
    "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8",
    "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8",
    "ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8",
    "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
    "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
    "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
    "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
    "ST_s-channel_4f_leptonDecays",
    "ST_s-channel_4f_hadronicDecays",
    "ST_t-channel_antitop_4f_InclusiveDecays",
    "ST_t-channel_antitop_5f_InclusiveDecays",
    "ST_t-channel_top_4f_InclusiveDecays",
    "ST_t-channel_top_5f_InclusiveDecays",
    "ST_tW_antitop_5f_inclusiveDecays",
    "ST_tW_antitop_5f_NoFullyHadronicDecays",
    "ST_tW_top_5f_inclusiveDecays",
    "ST_tW_top_5f_NoFullyHadronicDecays",
]
process_map["vv"] = [
    "WW_TuneCP5_13TeV-pythia8",
    "WZ_TuneCP5_13TeV-pythia8",
    "ZZ_TuneCP5_13TeV-pythia8",
    "WW",
    "WZ",
    "ZZ",
]
process_map["h125"] = [
    "GluGluHToWWToLNuQQ_M125_NNPDF31_TuneCP5_PSweights_13TeV_powheg_JHUGen710_pythia8",
    "GluGluHToWWToLNuQQ_M125_TuneCP5_PSweight_13TeV-powheg2-jhugen727-pythia8",
    "GluGluHToTauTau_M125_13TeV_powheg_pythia8",
    "VBFHToTauTau_M125_13TeV_powheg_pythia8",
    "WminusHToTauTau_M125_13TeV_powheg_pythia8",
    "WplusHToTauTau_M125_13TeV_powheg_pythia8",
    "ZHToTauTau_M125_13TeV_powheg_pythia8",
    "ggZH_HToTauTau_ZToLL_M125_13TeV_powheg_pythia8",
    "ggZH_HToTauTau_ZToNuNu_M125_13TeV_powheg_pythia8",
    "ggZH_HToTauTau_ZToQQ_M125_13TeV_powheg_pythia8",
    "ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8",
    "boostedTau_GluGluHTauTau_boostedTaua_13TeV_user",
    "GluGluHToTauTau",
    "VBFHToTauTau",
    "WminusHToTauTau",
    "WplusHToTauTau",
    "ZHToTauTau",
    "ttHToTauTau",
]
process_map["phi10"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M10_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M10_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi20"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M20_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M20_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi30"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M30_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M30_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi40"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M40_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M40_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi50"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M50_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M50_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi75"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M75_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M75_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi100"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M100_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M100_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi125"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M125_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M125_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi150"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M150_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M150_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi200"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M200_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M200_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi250"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M250_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M250_nodmx_v0_TuneCP5_MLM_nomatch",
]
process_map["phi300"] = [
    "Spin0ToTauTau_2j_scalar_g1_HT300_M300_nodmx_v0_TuneCP5_MLM",
    "Spin0ToTauTau_2j_scalar_g1_HT300_M300_nodmx_v0_TuneCP5_MLM_nomatch",
]
# process_map["phi10_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M10_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi20_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M20_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi30_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M30_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi40_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M40_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi50_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M50_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi75_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M75_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi100_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M100_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi125_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M125_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi150_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M150_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi200_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M200_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi250_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M250_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["phi300_unmatch"] = [
#    'Spin0ToTauTau_2j_scalar_g1_HT300_M300_nodmx_v0_TuneCP5_MLM_nomatch',
# ]
# process_map["ggF-Htt"] = [
#    'GluGluHToTauTau_M125_13TeV_powheg_pythia8',
# ]
# process_map["VBF-Htt"] = [
#    'VBFHToTauTau_M125_13TeV_powheg_pythia8',
# ]
# process_map["Wm-Htt"] = [
#    'WminusHToTauTau_M125_13TeV_powheg_pythia8',
# ]
# process_map["Wp-Htt"] = [
#    'WplusHToTauTau_M125_13TeV_powheg_pythia8',
# ]
# process_map["ZH-Htt"] = [
#    'ZHToTauTau_M125_13TeV_powheg_pythia8',
# ]
# process_map["ggZll-Htt"] = [
#    'ggZH_HToTauTau_ZToLL_M125_13TeV_powheg_pythia8',
# ]
# process_map["ggZvv-Htt"] = [
#    'ggZH_HToTauTau_ZToNuNu_M125_13TeV_powheg_pythia8',
# ]
# process_map["ggZqq-Htt"] = [
#    'ggZH_HToTauTau_ZToQQ_M125_13TeV_powheg_pythia8',
# ]
# process_map["tt-Htt"] = [
#    'ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8',
# ]
process_map["data"] = [
    "MET_Run2016B_ver2_HIPM",
    "MET_Run2016C_HIPM",
    "MET_Run2016D_HIPM",
    "MET_Run2016E_HIPM",
    "MET_Run2016F_HIPM",
    "SingleElectron_Run2016B_ver2_HIPM",
    "SingleElectron_Run2016C_HIPM",
    "SingleElectron_Run2016D_HIPM",
    "SingleElectron_Run2016E_HIPM",
    "SingleElectron_Run2016F_HIPM",
    "SingleMuon_Run2016B_ver2_HIPM",
    "SingleMuon_Run2016C_HIPM",
    "SingleMuon_Run2016D_HIPM",
    "SingleMuon_Run2016E_HIPM",
    "SingleMuon_Run2016F_HIPM",
    "MET_Run2016F",
    "MET_Run2016G",
    "MET_Run2016H",
    "SingleElectron_Run2016F",
    "SingleElectron_Run2016G",
    "SingleElectron_Run2016H",
    "SingleMuon_Run2016F",
    "SingleMuon_Run2016G",
    "SingleMuon_Run2016H",
    "SingleElectron_Run2017B",
    "SingleElectron_Run2017C",
    "SingleElectron_Run2017D",
    "SingleElectron_Run2017E",
    "SingleElectron_Run2017F",
    "SingleMuon_Run2017B",
    "SingleMuon_Run2017C",
    "SingleMuon_Run2017D",
    "SingleMuon_Run2017E",
    "SingleMuon_Run2017F",
    "MET_Run2017B",
    "MET_Run2017C",
    "MET_Run2017D",
    "MET_Run2017E",
    "MET_Run2017F",
    "SingleMuon_Run2018A",
    "SingleMuon_Run2018B",
    "SingleMuon_Run2018C",
    "SingleMuon_Run2018D",
    "MET_Run2018A",
    "MET_Run2018B",
    "MET_Run2018C",
    "MET_Run2018D",
    "EGamma_Run2018A",
    "EGamma_Run2018B",
    "EGamma_Run2018C",
    "EGamma_Run2018D",
]


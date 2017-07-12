from Gaudi.Configuration import importOptions
eventType = 21113001 
importOptions('$APPCONFIGOPTS/Gauss/Sim08-Beam3500GeV-md100-2011-nu2.py')
importOptions('$DECFILESROOT/options/21113001.py')
importOptions('$LBPYTHIA8ROOT/options/Pythia8.py')
importOptions('$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='Sim08-20130503',
    AppVersion='v45r3',
    XMLSummaryFile='summaryGaussv45r3.xml',
    Application='Gauss',
    OutputFilePrefix='00012345_00006789_1',
    RunNumber=5678,
    XMLFileCatalog='pool_xml_catalogGaussv45r3.xml',
    FirstEventNumber=1234,
    CondDBTag='Sim08-20130503-vc-md100',
    OutputFileTypes=['sim']
)

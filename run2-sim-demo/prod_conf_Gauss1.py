from Gaudi.Configuration import importOptions

eventType = 11198050 
importOptions('$APPCONFIGOPTS/Gauss/Beam6500GeV-mu100-2015-nu1.6.py')
importOptions('$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py')
importOptions('$APPCONFIGOPTS/Gauss/DataType-2015.py')
importOptions('$APPCONFIGOPTS/Gauss/RICHRandomHits.py')
importOptions('$DECFILESROOT/options/11198050.py')
importOptions('$LBPYTHIA8ROOT/options/Pythia8.py')
importOptions('$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20170721-3',
    AppVersion='v49r8',
    XMLSummaryFile='summaryGaussv49r8.xml',
    Application='Gauss',
    OutputFilePrefix='00012345_00006789_1',
    RunNumber=5678,
    XMLFileCatalog='pool_xml_catalogGaussv49r8.xml',
    FirstEventNumber=1234,
    CondDBTag='sim-20161124-vc-mu100',
    OutputFileTypes=['sim']
)

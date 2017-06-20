from Gaudi.Configuration import importOptions
eventType =11196082 
importOptions('$APPCONFIGOPTS/Gauss/Beam6500GeV-md100-2015-nu1.6.py')
importOptions('$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py')
importOptions('$APPCONFIGOPTS/Gauss/DataType-2015.py')
importOptions('$APPCONFIGOPTS/Gauss/RICHRandomHits.py')
importOptions('$DECFILESROOT/options/11196082.py')
importOptions('$LBPYTHIA8ROOT/options/Pythia8.py')
importOptions('$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20150724',
    AppVersion='v49r6',
    XMLSummaryFile='summaryGaussv49r6.xml',
    Application='Gauss',
    OutputFilePrefix='00012345_00006789_1',
    RunNumber=5678,
    XMLFileCatalog='pool_xml_catalogGaussv49r6.xml',
    FirstEventNumber=1234,
    CondDBTag='sim-20161124-vc-md100',
    OutputFileTypes=['sim']
)

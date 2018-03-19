from Gaudi.Configuration import importOptions
importOptions('$APPCONFIGOPTS/Boole/Default.py')
importOptions('$APPCONFIGOPTS/Boole/EnableSpillover.py')
importOptions('$APPCONFIGOPTS/Boole/DataType-2015.py')
importOptions('$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20170721-3',
    AppVersion='v30r2p1',
    InputFiles=['00012345_00006789_1.sim'],
    XMLSummaryFile='summaryBoolev30r2p1.xml',
    Application='Boole',
    OutputFilePrefix='00012345_00006789_2',
    XMLFileCatalog='pool_xml_catalogBoolev30r2p1.xml',
    CondDBTag='sim-20161124-vc-mu100',
    OutputFileTypes=['digi']
)

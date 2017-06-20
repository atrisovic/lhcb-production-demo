from Gaudi.Configuration import importOptions
eventType = None
importOptions('$APPCONFIGOPTS/Boole/Default.py')
importOptions('$APPCONFIGOPTS/Boole/EnableSpillover.py')
importOptions('$APPCONFIGOPTS/Boole/DataType-2015.py')
importOptions('$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20150724',
    AppVersion='v30r2',
    InputFiles=['00012345_00006789_1.sim'],
    XMLSummaryFile='summaryBoolev30r2.xml',
    Application='Boole',
    OutputFilePrefix='00012345_00006789_2',
    XMLFileCatalog='pool_xml_catalogBoolev30r2.xml',
    CondDBTag='sim-20161124-vc-md100',
    OutputFileTypes=['digi']
)

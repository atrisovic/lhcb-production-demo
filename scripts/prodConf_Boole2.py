from Gaudi.Configuration import importOptions
importOptions('$APPCONFIGOPTS/Boole/Default.py')
importOptions('$APPCONFIGOPTS/Boole/DataType-2011.py')
importOptions('$APPCONFIGOPTS/Boole/Boole-SiG4EnergyDeposit.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='Sim08-20130503',
    AppVersion='v26r3',
    InputFiles=['00012345_00006789_1.sim'],
    XMLSummaryFile='summaryBoolev26r3.xml',
    Application='Boole',
    OutputFilePrefix='00012345_00006789_2',
    XMLFileCatalog='pool_xml_catalogBoolev26r3.xml',
    CondDBTag='Sim08-20130503-vc-md100',
    OutputFileTypes=['digi']
)

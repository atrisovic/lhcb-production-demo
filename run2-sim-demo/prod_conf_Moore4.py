from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py')
importOptions('$APPCONFIGOPTS/Conditions/TCK-0x411400a2.py')
importOptions('$APPCONFIGOPTS/Moore/DataType-2015.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20170721-3',
    AppVersion='v24r2',
    InputFiles=['00012345_00006789_3.digi'],
    XMLSummaryFile='summaryMoorev24r2.xml',
    Application='Moore',
    OutputFilePrefix='00012345_00006789_4',
    XMLFileCatalog='pool_xml_catalogMoorev24r2.xml',
    CondDBTag='sim-20161124-vc-mu100',
    OutputFileTypes=['digi']
)


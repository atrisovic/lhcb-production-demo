from Gaudi.Configuration import importOptions
eventType = None
importOptions('$APPCONFIGOPTS/L0App/L0AppSimProduction.py')
importOptions('$APPCONFIGOPTS/L0App/L0AppTCK-0x00a2.py')
importOptions('$APPCONFIGOPTS/L0App/ForceLUTVersionV8.py')
importOptions('$APPCONFIGOPTS/L0App/DataType-2015.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    OptionFormat='l0app',
    DDDBTag='dddb-20150724',
    AppVersion='v24r2',
    InputFiles=['00012345_00006789_2.digi'],
    XMLSummaryFile='summaryMoorev24r2.xml',
    Application='Moore',
    OutputFilePrefix='00012345_00006789_3',
    XMLFileCatalog='pool_xml_catalogMoorev24r2.xml',
    CondDBTag='sim-20161124-vc-md100',
    OutputFileTypes=['digi']
)

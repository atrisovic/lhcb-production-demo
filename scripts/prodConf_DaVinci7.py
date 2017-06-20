from Gaudi.Configuration import importOptions
eventType = None
importOptions('$APPCONFIGOPTS/DaVinci/DataType-2015.py')
importOptions('$APPCONFIGOPTS/DaVinci/InputType-DST.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')
importOptions('$SEMILEPCONFIGOPTS/Filter_DplusTauNu_S24.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20150724',
    AppVersion='v38r1p1',
    InputFiles=['00012345_00006789_5.dst'],
    XMLSummaryFile='summaryDaVinciv38r1p1.xml',
    Application='DaVinci',
    OutputFilePrefix='00012345_00006789_7',
    XMLFileCatalog='pool_xml_catalogDaVinciv38r1p1.xml',
    CondDBTag='sim-20161124-vc-md100',
    OutputFileTypes=['dst']
)

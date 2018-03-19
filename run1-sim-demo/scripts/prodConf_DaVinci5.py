from Gaudi.Configuration import importOptions
importOptions('$APPCONFIGOPTS/DaVinci/DV-Stripping20r1-Stripping-MC-NoPrescaling.py')
importOptions('$APPCONFIGOPTS/DaVinci/DataType-2011.py')
importOptions('$APPCONFIGOPTS/DaVinci/InputType-DST.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='Sim08-20130503',
    AppVersion='v32r2p3',
    InputFiles=['00012345_00006789_4.dst'],
    XMLSummaryFile='summaryDaVinciv32r2p3.xml',
    Application='DaVinci',
    OutputFilePrefix='00012345_00006789_5',
    XMLFileCatalog='pool_xml_catalogDaVinciv32r2p3.xml',
    CondDBTag='Sim08-20130503-vc-md100',
    OutputFileTypes=['dst']
)

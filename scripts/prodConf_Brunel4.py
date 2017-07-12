from Gaudi.Configuration import importOptions
importOptions('$APPCONFIGOPTS/Brunel/DataType-2011.py')
importOptions('$APPCONFIGOPTS/Brunel/MC-WithTruth.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='Sim08-20130503',
    AppVersion='v43r2p7',
    InputFiles=['00012345_00006789_3.digi'],
    XMLSummaryFile='summaryBrunelv43r2p7.xml',
    Application='Brunel',
    OutputFilePrefix='00012345_00006789_4',
    XMLFileCatalog='pool_xml_catalogBrunelv43r2p7.xml',
    CondDBTag='Sim08-20130503-vc-md100',
    OutputFileTypes=['dst']
)

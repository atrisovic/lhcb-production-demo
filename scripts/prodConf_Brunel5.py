from Gaudi.Configuration import importOptions
eventType = None
importOptions('$APPCONFIGOPTS/Brunel/DataType-2015.py')
importOptions('$APPCONFIGOPTS/Brunel/MC-WithTruth.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20150724',
    AppVersion='v48r2p1',
    InputFiles=['00012345_00006789_4.digi'],
    XMLSummaryFile='summaryBrunelv48r2p1.xml',
    Application='Brunel',
    OutputFilePrefix='00012345_00006789_5',
    XMLFileCatalog='pool_xml_catalogBrunelv48r2p1.xml',
    CondDBTag='sim-20161124-vc-md100',
    OutputFileTypes=['dst']
)

from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Brunel/DataType-2012.py')
importOptions('$APPCONFIGOPTS/Brunel/MC-WithTruth.py')
importOptions('$APPCONFIGOPTS/Brunel/Sim09-Run1.py')
importOptions('$APPCONFIGOPTS/Persistency/DST-multipleTCK-2012.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20150928',
    AppVersion='v43r2p11',
    InputFiles=['output_moore.dst'],
    XMLSummaryFile='summary_brunel.xml',
    Application='Brunel',
    OutputFilePrefix='output_brunel',
    XMLFileCatalog='pool_xml_catalog_brunel.xml',
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['dst']
)

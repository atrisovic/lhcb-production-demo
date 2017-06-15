from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Boole/Default.py')
importOptions('$APPCONFIGOPTS/Boole/DataType-2012.py')
importOptions('$APPCONFIGOPTS/Boole/NoPacking.py')
importOptions('$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=2,
    DDDBTag='dddb-20150928',
    AppVersion='v30r1',
    InputFiles=['1/file.sim'],
    XMLSummaryFile='./2/summary.xml',
    Application='Boole',
    OutputFilePrefix='./2/file',
    RunNumber=12345,
    XMLFileCatalog='./2/pool_xml_catalog.xml',
    FirstEventNumber=6789,
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['digi']
)

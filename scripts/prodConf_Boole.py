from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Boole/Default.py')
importOptions('$APPCONFIGOPTS/Boole/DataType-2012.py')
importOptions('$APPCONFIGOPTS/Boole/NoPacking.py')
importOptions('$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20150928',
    AppVersion='v30r1',
    InputFiles=['output_gauss.sim'],
    XMLSummaryFile='summary_boole.xml',
    Application='Boole',
    OutputFilePrefix='output_boole',
    RunNumber=12345,
    XMLFileCatalog='pool_xml_catalog_boole.xml',
    FirstEventNumber=6789,
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['digi']
)

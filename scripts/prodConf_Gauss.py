from Gaudi.Configuration import importOptions
eventType = 12113111
importOptions('$APPCONFIGOPTS/Gauss/Sim08-Beam4000GeV-mu100-2012-nu2.5.py')
importOptions('$APPCONFIGOPTS/Gauss/DataType-2012.py')
importOptions('$APPCONFIGOPTS/Gauss/RICHRandomHits.py')
importOptions('$APPCONFIGOPTS/Gauss/NoPacking.py')
importOptions('$DECFILESROOT/options/12113111.py')
importOptions('$LBPYTHIA8ROOT/options/Pythia8.py')
importOptions('$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py')
importOptions('$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=2,
    DDDBTag='dddb-20150928',
    AppVersion='v49r1',
    XMLSummaryFile='./1/summary.xml',
    Application='Gauss',
    OutputFilePrefix='./1/file',
    RunNumber=12345,
    XMLFileCatalog='./1/pool_xml_catalog.xml',
    FirstEventNumber=6789,
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['sim']
)

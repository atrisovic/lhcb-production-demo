from Gaudi.Configuration import importOptions
importOptions('$APPCONFIGOPTS/DaVinci/DV-Stripping24r1-Stripping-MC-NoPrescaling-DST.py')
importOptions('$APPCONFIGOPTS/DaVinci/DV-Stripping-MC-muDST.py')
importOptions('$APPCONFIGOPTS/DaVinci/DataType-2015.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20170721-3',
    AppVersion='v38r1p6',
    InputFiles=['00012345_00006789_5.dst'],
    XMLSummaryFile='summaryDaVinciv38r1p6.xml',
    Application='DaVinci',
    OutputFilePrefix='ALLSTREAMS',
    XMLFileCatalog='pool_xml_catalogDaVinciv38r1p6.xml',
    CondDBTag='sim-20161124-vc-mu100',
    OutputFileTypes=['mdst']
)


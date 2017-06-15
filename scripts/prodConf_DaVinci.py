from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/DaVinci/DV-Stripping21-Stripping-MC-NoPrescaling.py')
importOptions('$APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py')
importOptions('$APPCONFIGOPTS/DaVinci/DataType-2012.py')
importOptions('$APPCONFIGOPTS/DaVinci/InputType-DST.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=2,
    DDDBTag='dddb-20150928',
    AppVersion='v36r1p3',
    InputFiles=['output_brunel.dst'],
    XMLSummaryFile='summary_davinci.xml',
    Application='DaVinci',
    OutputFilePrefix='allstreams',
    XMLFileCatalog='pool_xml_catalog_davinci.xml',
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['dst']
)

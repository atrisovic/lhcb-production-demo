from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/L0App/L0AppSimProduction.py')
importOptions('$APPCONFIGOPTS/L0App/L0AppTCK-0x0045.py')
importOptions('$APPCONFIGOPTS/L0App/DataType-2012.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=2,
    OptionFormat='l0app',
    DDDBTag='dddb-20150928',
    AppVersion='v20r4',
    InputFiles=['2/file.digi'],
    XMLSummaryFile='./3/summary.xml',
    Application='Moore',
    OutputFilePrefix='./3/file',
    XMLFileCatalog='./3/pool_xml_catalog.xml',
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['digi']
)

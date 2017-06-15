from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/L0App/L0AppSimProduction.py')
importOptions('$APPCONFIGOPTS/L0App/L0AppTCK-0x0045.py')
importOptions('$APPCONFIGOPTS/L0App/DataType-2012.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    OptionFormat='l0app',
    DDDBTag='dddb-20150928',
    AppVersion='v20r4',
    InputFiles=['output_boole.digi'],
    XMLSummaryFile='summary_moorel0.xml',
    Application='Moore',
    OutputFilePrefix='output_moorel0',
    XMLFileCatalog='pool_xml_catalog_moorel0.xml',
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['digi']
)

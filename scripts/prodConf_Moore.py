from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep.py')
importOptions('$APPCONFIGOPTS/Conditions/TCK-0x409f0045.py')
importOptions('$APPCONFIGOPTS/Moore/DataType-2012.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20150928',
    AppVersion='v14r8p1',
    InputFiles=['output_moorel0.digi'],
    XMLSummaryFile='summary_moore.xml',
    Application='Moore',
    OutputFilePrefix='output_moore',
    XMLFileCatalog='pool_xml_catalog.xml',
    CondDBTag='sim-20160321-2-vc-mu100',
    OutputFileTypes=['digi']
)

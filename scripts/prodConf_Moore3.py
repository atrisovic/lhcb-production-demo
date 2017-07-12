from Gaudi.Configuration import importOptions
importOptions('$APPCONFIGOPTS/Moore/MooreSimProductionWithL0Emulation.py')
importOptions('$APPCONFIGOPTS/Conditions/TCK-0x40760037.py')
importOptions('$APPCONFIGOPTS/Moore/DataType-2011.py')
importOptions('$APPCONFIGOPTS/L0/L0TCK-0x0037.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='Sim08-20130503',
    AppVersion='v12r8g3',
    InputFiles=['00012345_00006789_2.digi'],
    XMLSummaryFile='summaryMoorev12r8g3.xml',
    Application='Moore',
    OutputFilePrefix='00012345_00006789_3',
    XMLFileCatalog='pool_xml_catalogMoorev12r8g3.xml',
    CondDBTag='Sim08-20130503-vc-md100',
    OutputFileTypes=['digi']
)

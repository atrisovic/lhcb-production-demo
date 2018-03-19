from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/Turbo/Tesla_AllHlt2Lines_v10r0_0x00fa0051.py')
importOptions('$APPCONFIGOPTS/Turbo/Tesla_Simulation_2015_PVHLT2.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    DDDBTag='dddb-20170721-3',
    AppVersion='v40r1p3',
    OptionFormat='Tesla',
    InputFiles=['00012345_00006789_5.dst'],
    XMLSummaryFile='summaryDaVinciv40r1p3.xml',
    Application='DaVinci',
    OutputFilePrefix='TURBO',
    XMLFileCatalog='pool_xml_catalogDaVinciv40r1p3.xml',
    CondDBTag='sim-20161124-vc-mu100',
    OutputFileTypes=['dst']
)




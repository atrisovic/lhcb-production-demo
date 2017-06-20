from Gaudi.Configuration import importOptions
eventType = None
importOptions('$APPCONFIGOPTS/Turbo/Tesla_AllHlt2Lines_v10r0_0x00fa0051.py')
importOptions('$APPCONFIGOPTS/Turbo/Tesla_Simulation_2015_PVHLT2.py')

from ProdConf import ProdConf

ProdConf(
    NOfEvents=1,
    OptionFormat='Tesla',
    DDDBTag='dddb-20150724',
    AppVersion='v40r1p3',
    InputFiles=['00012345_00006789_5.dst'],
    XMLSummaryFile='summaryDaVinciv40r1p3.xml',
    Application='DaVinci',
    OutputFilePrefix='00012345_00006789_6',
    XMLFileCatalog='pool_xml_catalogDaVinciv40r1p3.xml',
    CondDBTag='fromPreviousStep',
    OutputFileTypes=['dst']
)

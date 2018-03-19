#!/bin/bash

source  /cvmfs/lhcb.cern.ch/lib/LbLogin.sh --no-userarea
LbLogin -c x86_64-slc5-gcc46-opt 

# simulation
lb-run --use ProdConf --use  AppConfig.v3r171 --use DecFiles.v27r6 Gauss/v45r3 gaudirun.py prodConf_Gauss1.py
# digitization
lb-run --use AppConfig.v3r171 --use ProdConf Boole/v26r3 gaudirun.py prodConf_Boole2.py
# trigger
LbLogin -c x86_64-slc5-gcc43-opt 
lb-run --use AppConfig.v3r171 --use ProdConf Moore/v12r8g3 gaudirun.py prodConf_Moore3.py
# reconstruction
lb-run --use AppConfig.v3r171 --use ProdConf Brunel/v43r2p7 gaudirun.py prodConf_Brunel4.py
# stripping
lb-run --use AppConfig.v3r171 --use ProdConf DaVinci/v32r2p3 gaudirun.py prodConf_DaVinci5.py

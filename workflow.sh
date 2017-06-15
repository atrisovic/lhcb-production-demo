#!/bin/bash
export USER=`whoami`
source  /cvmfs/lhcb.cern.ch/lib/LbLogin.sh --no-userarea

# simulation
lb-run --use AppConfig.v3r277 --use DecFiles.v29r5 --use ProdConf Gauss/v49r1 gaudirun.py prodConf_Gauss.py
# digitization
lb-run --use AppConfig.v3r266 --use ProdConf Boole v30r1 gaudirun.py prodConf_Boole.py
# l0_trigger
LbLogin -c x86_64-slc6-gcc46-opt
lb-run --use AppConfig.v3r200 --use ProdConf Moore v20r4 gaudirun.py prodConf_MooreL0.py
# hlt
LbLogin -c x86_64-slc5-gcc46-opt
lb-run --use "AppConfig v3r241" --use ProdConf Moore v14r8p1 gaudirun.py prodConf_Moore.py
# reconstruction
LbLogin -c x86_64-slc5-gcc46-opt 
lb-run --use "AppConfig v3r246" --use ProdConf Brunel v43r2p11 gaudirun.py prodConf_Brunel.py
# stripping
LbLogin -c x86_64-slc6-gcc48-opt
lb-run --use "AppConfig v3r277" --use ProdConf DaVinci v36r1p3 gaudirun.py prodConf_DaVinci.py


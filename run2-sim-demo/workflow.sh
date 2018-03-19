#!/bin/bash
set -e
source  /cvmfs/lhcb.cern.ch/lib/LbLogin.sh --no-userarea
LbLogin -c x86_64-slc6-gcc48-opt

# 1 simulation
lb-run --use ProdConf --use AppConfig.v3r335 --use DecFiles.v30r9 Gauss/v49r8 gaudirun.py prod_conf_Gauss1.py
# 2 digitization
LbLogin -c x86_64-slc6-gcc49-opt
lb-run --use AppConfig.v3r338 --use ProdConf Boole/v30r2p1 gaudirun.py prod_conf_Boole2.py
# 3 trigger
LbLogin -c x86_64-slc6-gcc48-opt
lb-run --use AppConfig.v3r268 --use ProdConf Moore/v24r2 gaudirun.py prod_conf_Moore3.py
# 4 hlt
lb-run --use AppConfig.v3r268 --use ProdConf Moore/v24r2 gaudirun.py prod_conf_Moore4.py
# 5 reconstruction
lb-run --use AppConfig.v3r277 --use SQLDDDB.v7r10 --use ProdConf Brunel/v48r2p1 gaudirun.py prod_conf_Brunel5.py
# 6 turbo
lb-run --use AppConfig.v3r232 --use TurboStreamProd.v2r0 --use ProdConf DaVinci/v40r1p3 gaudirun.py prod_conf_Tesla6.py
# 7 stripping
LbLogin -c x86_64-slc6-gcc49-opt
lb-run --use AppConfig.v3r343 --use ProdConf DaVinci/v38r1p6 gaudirun.py prod_conf_DaVinci7.py



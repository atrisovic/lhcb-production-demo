#!/bin/bash

# simulation
lb-run --use ProdConf --use AppConfig.v3r304 --use DecFiles.v29r16 Gauss/v49r6 gaudirun.py prodConf_Gauss1.py
# digitization
lb-run --use AppConfig.v3r304 --use ProdConf Boole/v30r2 gaudirun.py prodConf_Boole2.py
# l0_trigger
lb-run --use AppConfig.v3r268 --use ProdConf Moore/v24r2 gaudirun.py prodConf_Moore3.py
# hlt
lb-run --use AppConfig.v3r268 --use ProdConf Moore/v24r2 gaudirun.py prodConf_Moore4.py
# reconstruction
lb-run --use AppConfig.v3r277 --use SQLDDDB.v7r10 --use ProdConf Brunel/v48r2p1 gaudirun.py prodConf_Brunel5.py
# turbo 
lb-run --use AppConfig.v3r232 --use TurboStreamProd.v2r0 --use ProdConf DaVinci/v40r1p3 gaudirun.py prodConf_DaVinci6.py
# stripping
lb-run --use AppConfig.v3r296 --use SemilepConfig.v1r15 --use ProdConf DaVinci/v38r1p1 gaudirun.py prodConf_DaVinci7.py

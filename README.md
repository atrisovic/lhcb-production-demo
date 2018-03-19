# LHCb production demo

Simple Monte Carlo production chain.

## Data simulated

This sample was used in [atrisovic/analysis-case-study](https://github.com/atrisovic/analysis-case-study). 
Bookkeeping path: `MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia8/Sim08a/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/21113001`

More info:
```
ID: 12704
Name: Charm WG: Greening D->hmumu - Sim08a Model for 2011 data - MD - Pythia8
Type: Simulation
State: Done
Event type: 21113001 D+_K+mumu=DecProdCut
```

## Instructions

Build and run the image with:

```
$ docker build -t prod .
docker run -v /cvmfs:/cvmfs:Z -it --rm prod /bin/bash 
```

## Troubleshooting

Error: `line 3: /cvmfs/lhcb.cern.ch/lib/LbLogin.sh: Too many levels of symbolic links`
Solution: Exit container and run again.


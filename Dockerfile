FROM lhcbdev/slc6-build 
MAINTAINER Ana Trisovic "ana.trisovic@cern.ch"

WORKDIR "/workspace"

COPY scripts/* /workspace/
COPY workflow.sh /workspace/

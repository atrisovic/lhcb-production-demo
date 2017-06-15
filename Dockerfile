FROM hepsw/cvmfs-lhcb
MAINTAINER Ana Trisovic "ana.trisovic@cern.ch"

WORKDIR "/workspace"

COPY scripts/* /workspace/
COPY workflow.sh /workspace/

#RUN /workflow.sh


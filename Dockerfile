FROM hepsw/cvmfs-lhcb
MAINTAINER Ana Trisovic "ana.trisovic@cern.ch"

RUN yum -y reinstall glibc; exit 0
WORKDIR "/workspace"

COPY scripts/* /workspace/
COPY workflow.sh /workspace/



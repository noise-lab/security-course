FROM ubuntu:14.04
MAINTAINER Simon Kim <skim104@illinois.edu>

RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -y tcpdump

WORKDIR /root

ENTRYPOINT [ "/usr/sbin/tcpdump" ]

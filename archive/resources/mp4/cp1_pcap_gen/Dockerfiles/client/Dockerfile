FROM ubuntu:14.04
MAINTAINER Simon Kim <skim104@illinois.edu>

RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -y ssh sshpass ftp wget

ADD start.sh /root/
RUN chmod +x /root/start.sh

ENTRYPOINT [ "/root/start.sh" ]

FROM debian:jessie

MAINTAINER Simon Kim <skim104@illinois.edu>

RUN apt-get update && apt-get install -y vsftpd

ADD vsftpd.conf /etc/
ADD vsftpd.sh /root/

RUN mkdir -p /var/run/vsftpd/empty
RUN chmod +x /root/vsftpd.sh
RUN chown root:root /etc/vsftpd.conf

VOLUME /ftp/

EXPOSE 21

ENTRYPOINT [ "/root/vsftpd.sh" ]
CMD [ "vsftpd" ]

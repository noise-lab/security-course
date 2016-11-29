#!/bin/bash
# docker setup for ubuntu 14.04 amd64
# check if root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi
apt-get update
apt-get install -y apt-transport-https ca-certificates

# install docker
# new GPG key
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
# add apt source
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
apt-get update
apt-get purge lxc-docker
apt-cache policy docker-engine

# verify repo
read -n1 -r -p "verify the output, and press spacebar to continue..." key

if [ "$key" != '' ]; then
    # Anything else pressed, do whatever else.
    echo "aborting..."
    exit 1
fi

# prereq
apt-get update
apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual

# install docker
apt-get update
apt-get install -y docker-engine

# build images
docker rmi $(docker images -aq)
docker build -t mp4.1_client ../Dockerfiles/client/
docker build -t mp4.1_nmap ../Dockerfiles/nmap/
docker build -t mp4.1_ssh ../Dockerfiles/ssh/
docker build -t mp4.1_active_ftp ../Dockerfiles/active_ftp/
docker build -t mp4.1_passive_ftp ../Dockerfiles/passive_ftp/
docker build -t mp4.1_tcpdump ../Dockerfiles/tcpdump/

# install sshpass
apt-get install -y sshpass

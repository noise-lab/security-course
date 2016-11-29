#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
        echo "sudo plz"
        exit 1
fi

# check arguments
if [ "$#" -ne 2 ]; then
    echo "usage: ./common_setup.sh {hostname} {username}"
    exit 1
fi

# set hostname
scutil --set ComputerName $1
scutil --set LocalHostName $1
scutil --set HostName $1
dscacheutil -flushcache

# set vimrc
cp -r ./vim/.vim ~/
cp ./vim/.vimrc ~/

# copy authorized_keys
mkdir ~/.ssh
chown $2 ~/.ssh
cp ./ssh/authorized_keys ~/.ssh
chown $2 ~/.ssh/authorized_keys
chmod go-w ~/
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# sshd config
cp ./ssh/sshd_config /etc/sshd_config
chown root /etc/sshd_config
chmod 644 /etc/sshd_config

# install coffeescript
npm install -g coffee-script

# install npm packages
cd ./website
npm install
cd ../

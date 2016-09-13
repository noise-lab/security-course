#!/bin/sh

set -e
set -o xtrace

user=${USER:-ftpuser}
password=${PASSWORD:-changeme}
dir=${DIR:-/ftp}

useradd --home-dir ${dir} --no-create-home $user

echo "$1" >> "${dir}/flag.txt"

echo "$user:$password" | chpasswd
echo "Login info is: $user:$password"

exec vsftpd

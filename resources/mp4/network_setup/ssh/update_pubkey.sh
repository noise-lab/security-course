#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
        echo "sudo plz"
        exit 1
fi

# check arguments
if [ "$#" -ne 1 ]; then
    echo "usage: sudo ./update_pubkey.sh {username}"
    exit 1
fi

cp authorized_keys ~/.ssh
chown $1 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

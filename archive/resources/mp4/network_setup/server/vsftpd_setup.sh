#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
    echo "sudo plz"
    exit 1
fi

# unload from launchd
launchctl stop /Library/LaunchDaemons/vsftpd.plist
launchctl unload /Library/LaunchDaemons/vsftpd.plist

# copy vsftpd conf
cp ./vsftpd/vsftpd.conf /usr/local/etc/
chown root /usr/local/etc/vsftpd.conf

# copy private key to shared location
cp /etc/apache2/server* ~/Public

# copy launchd plist
cp ./vsftpd/vsftpd.plist /Library/LaunchDaemons/
chown root /Library/LaunchDaemons/vsftpd.plist

# load to launchd
launchctl load /Library/LaunchDaemons/vsftpd.plist

#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
    echo "sudo plz"
    exit 1
fi

# unload from launchd
launchctl stop /System/Library/LaunchDaemons/bootps.plist
launchctl unload /System/Library/LaunchDaemons/bootps.plist
rm /var/db/dhcpd_leases

# copy bootpd.plist
cp ./dhcp/bootpd.plist /etc/bootpd.plist
cp ./dhcp/bootptab /etc/bootptab

# load to launchd
launchctl load -w /System/Library/LaunchDaemons/bootps.plist

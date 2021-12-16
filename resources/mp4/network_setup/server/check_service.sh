#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
    echo "sudo plz"
    exit 1
fi

# check apache2
output=$(launchctl list | grep 'org.apache.httpd')
if [ "${output}" = "" ]; then
    echo "httpd not running"
    echo "  try sudo apachectl start"
else
    echo "httpd running"
fi

# check vsftpd
output=$(launchctl list | grep 'vsftpd')
if [ "${output}" = "" ]; then
    echo "vsftpd not running"
    echo "  try sudo launchctl load /Library/LaunchDaemons/vsftpd.plist"
    echo "  or sudo launchctl start /Library/LaunchDaemons/vsftpd.plist"
else
    echo "vsftpd running"
fi

# check bootpd
output=$(launchctl list | grep 'com.apple.bootpd')
if [ "${output}" = "" ]; then
    echo "dhcp not running"
    echo "  try sudo launchctl load -w /System/Library/LaunchDaemons/bootps.plist"
    echo "  or sudo launchctl start /System/Library/LaunchDaemons/bootps.plist"
else
    echo "dhcp running"
fi

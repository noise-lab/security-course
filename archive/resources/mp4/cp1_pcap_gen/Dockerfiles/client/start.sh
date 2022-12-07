#!/bin/bash
sshpass -p "changeme" scp -q -o LogLevel=QUIET -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@$1:/oops.png /dev/null 2>&1 > /dev/null
wget -qO- ftp://ftpuser:changeme@$2/flag.txt 2>&1 > /dev/null
ping -c 1 8.8.4.4 > /dev/null
wget -qO- ftp://ftpuser:changeme@$3/flag.txt 2>&1 > /dev/null
nc -lu -w 1 9000

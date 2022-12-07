#!/bin/bash
nmap -sU --top-ports 10 "$1"
while ! nc -vuz $2 9000 ; do sleep 1; done
exit

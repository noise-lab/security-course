#!/bin/bash

COUNT=0
MAX=1
SERVER_COUNT=0
SERVER_MAX=3
FREQ=5

cd ../website

while [ 1 ]; do
    DATE=$(date "+%y%m%d")
    TIME=$(date "+%H:%M:%S")
    RET=$(coffee client.coffee)
    echo ${RET}
    echo "${TIME} ${RET}" >> ~/Desktop/creds-${DATE}.txt
    CODE=$(echo ${RET} | awk '{print $2}')
    if [ "${CODE}" = "200" ]; then
        COUNT=0
        SERVER_COUNT=0
        sleep ${FREQ}
    else
        echo "Error"
        (( COUNT += 1 ))
        if [ "${COUNT}" -ge "${MAX}" ]; then
            (( SERVER_COUNT += 1 ))
            networksetup -setairportpower en1 off
            sleep 5
            networksetup -setairportpower en1 on
            if [ "${SERVER_COUNT}" -eq 1 ]; then
                ../client/send_alert.py "Something was wrong with client and the wifi adapter was reset."
            elif [ "${SERVER_COUNT}" -eq "${SERVER_MAX}" ]; then
                ../client/send_alert.py "Wifi reset didn't seem to fix the issue. Check the server as well."
                SERVER_COUNT=1
            fi
            COUNT=0
        fi
    fi
done

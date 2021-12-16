#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
  echo "sudo plz"
  exit 1
fi

# check arguments
if [ "$#" -ne 5 ]; then
  echo "usage: sudo ./capture_traffic.sh {subnet1} {subnet2} {active_ftp_message} {passive_ftp_message} {output_dir}"
  exit 1
fi

echo $1
echo $2
SUBNET="10.$1.$2"
GW_IP="${SUBNET}.1"
MSG_ACTIVE="$3"
MSG_PASSIVE="$4"
OUTPUT_DIR="$5"
IP=($(shuf -i 2-253 -n 5))
IP1="${SUBNET}.${IP[0]}"
IP2="${SUBNET}.${IP[1]}"
IP3="${SUBNET}.${IP[2]}"
IP4="${SUBNET}.${IP[3]}"
PORTSCAN_IP="${IP4}"
IP5="${SUBNET}.${IP[4]}"

# create network
docker network create --subnet="${SUBNET}.0/24" "tempnet" 2>&1 > /dev/null
INTERFACE="br-$(docker network ls | grep "tempnet" | awk '{print $1}')"
GW_MAC=$(ip link show ${INTERFACE} | awk '/ether/ {print $2}')

# sshd container
docker run -d --name "sshd" --net "tempnet" --ip "${IP1}" mp4.1_ssh 2>&1 > /dev/null
MAC1=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' "sshd")
# check if ready
while true; do
  sshpass -p "changeme" scp -q -o LogLevel=QUIET -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@${IP1}:/oops.png /dev/null 2>&1 > /dev/null
  if [ "$?" -eq 0 ]; then
    break
  fi
  sleep 1
done

# passive ftp container
docker run -d --name "passive_ftp" --net "tempnet" --ip "${IP2}" mp4.1_passive_ftp "${MSG_PASSIVE}" 2>&1 > /dev/null
MAC2=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' "passive_ftp")
# check if ready
while true; do
  wget -qO- ftp://ftpuser:changeme@${IP2}/flag.txt 2>&1 > /dev/null
  if [ "$?" -eq 0 ]; then
    break
  fi
  sleep 1
done

# active ftp container
docker run -d --name "active_ftp" --net "tempnet" --ip "${IP3}" mp4.1_active_ftp "${MSG_ACTIVE}" 2>&1 > /dev/null
MAC3=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' "active_ftp")
# check if ready
while true; do
  wget -qO- ftp://ftpuser:changeme@${IP3}/flag.txt 2>&1 > /dev/null
  if [ "$?" -eq 0 ]; then
    break
  fi
  sleep 1
done

# start capturing with tcpdump container
docker run -d --name "tcpdump" --net=host -v ${OUTPUT_DIR}:/root mp4.1_tcpdump -n "ip" -i "${INTERFACE}" -w "/root/4.1.1.pcap" 2>&1 >/dev/null

# client container
docker run -d --name "client" --net "tempnet" --ip "${IP5}" mp4.1_client ${IP1} ${IP3} ${IP2} 2>&1 > /dev/null
MAC5=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' "client")

# nmap container
docker run -d --name "nmap" --net "tempnet" --ip "${IP4}" mp4.1_nmap ${IP1} ${IP5} 2>&1 > /dev/null
MAC4=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' "nmap")

# check if everything is done
while true; do
  STATUS=$(docker ps -a | grep "nmap" | grep "Exited")
  if [ "${STATUS}" != "" ]; then
    break
  fi
  sleep 1
done

# container cleanup
docker stop "tcpdump" 2>&1 > /dev/null
docker kill $(docker ps -q) 2>&1 > /dev/null
docker rm $(docker ps -aq) 2>&1 > /dev/null
docker network rm "tempnet" 2>&1 > /dev/null

# printout answers in json
printf '"mac":["%s","%s","%s","%s","%s","%s"], "ip":["%s","%s","%s","%s","%s","%s"], "gw":"%s", "active":"%s", "passive":"%s", "portscan":"%s",' \
  "${GW_MAC}" "${MAC1}" "${MAC2}" "${MAC3}" "${MAC4}" "${MAC5}" \
  "${GW_IP}" "${IP1}" "${IP2}" "${IP3}" "${IP4}" "${IP5}" \
  "${GW_IP}" \
  "${MSG_ACTIVE}" \
  "${MSG_PASSIVE}" \
  "${PORTSCAN_IP}"

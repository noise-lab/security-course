#!/bin/bash
# check if root
if [ "$(id -u)" != "0" ]; then
  echo "sudo plz"
  exit 1
fi

# check arguments
if [ "$#" -ne 3 ]; then
  echo "usage: sudo ./pcap_gen.sh {local_svn_repo} {roster_filepath} {text_file} in absolute paths"
  exit 1
fi
if [ ! -d "$1" ]; then
  echo "$1 does not exist. Provide a valid path."
  exit 1
fi
if [ ! -f "$2" ]; then
  echo "$2 does not exist. Provide a valid path."
  exit 1
fi
if [ ! -f "$3" ]; then
  echo "$3 does not exist. Provide a valid path."
  exit 1
fi
WORKING_DIR="${PWD}"
SOL="${WORKING_DIR}/cp1_sol_temp.json"
LOCAL_SVN="$1"
ROSTER_FILE="$2"
MAX_ROSTER=$(cat ${ROSTER_FILE} | wc -l)
TXT_FILE="$3"
MSG_FILE="${WORKING_DIR}/messages.txt"
${WORKING_DIR}/scripts/format_msg.sh "${TXT_FILE}" "${MSG_FILE}"
MAX_MSG=$(cat ${MSG_FILE} | wc -l)
PCAP1_SUBNET1=($(shuf -i 0-255 -n ${MAX_ROSTER}))
PCAP1_SUBNET2=($(shuf -i 0-255 -n ${MAX_ROSTER}))
PCAP1_MSG_ACTIVE=($(shuf -i 1-${MAX_MSG} -n ${MAX_ROSTER}))
PCAP1_MSG_PASSIVE=($(shuf -i 1-${MAX_MSG} -n ${MAX_ROSTER}))
PCAP2_MSG=($(shuf -i 1-${MAX_MSG} -n ${MAX_ROSTER}))

COUNT=0
printf '{"%s":{"%s":"%s", "%s":"%s", "%s":"%s", "%s":["%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"], "%s":"%s", "%s":"%s", "%s":"%s"},' \
  "common" \
  "tcp" "5" \
  "year" "2012" \
  "hostname" "www.facebook.com" \
  "ciphersuite-list" "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (0xc00a)" "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (0xc014)" "TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA (0x0088)" "TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA (0x0087)" "TLS_DHE_RSA_WITH_AES_256_CBC_SHA (0x0039)" "TLS_DHE_DSS_WITH_AES_256_CBC_SHA (0x0038)" "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA (0xc00f)" "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA (0xc005)" "TLS_RSA_WITH_CAMELLIA_256_CBC_SHA (0x0084)" "TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)" "TLS_ECDHE_ECDSA_WITH_RC4_128_SHA (0xc007)" "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA (0xc009)" "TLS_ECDHE_RSA_WITH_RC4_128_SHA (0xc011)" "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (0xc013)" "TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA (0x0045)" "TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA (0x0044)" "TLS_DHE_DSS_WITH_RC4_128_SHA (0x0066)" "TLS_DHE_RSA_WITH_AES_128_CBC_SHA (0x0033)" "TLS_DHE_DSS_WITH_AES_128_CBC_SHA (0x0032)" "TLS_ECDH_RSA_WITH_RC4_128_SHA (0xc00c)" "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA (0xc00e)" "TLS_ECDH_ECDSA_WITH_RC4_128_SHA (0xc002)" "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA (0xc004)" "TLS_RSA_WITH_SEED_CBC_SHA (0x0096)" "TLS_RSA_WITH_CAMELLIA_128_CBC_SHA (0x0041)" "TLS_RSA_WITH_RC4_128_SHA (0x0005)" "TLS_RSA_WITH_RC4_128_MD5 (0x0004)" "TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)" "TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA (0xc008)" "TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA (0xc012)" "TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA (0x0016)" "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA (0x0013)" "TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA (0xc00d)" "TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA (0xc003)" "SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA (0xfeff)" "TLS_RSA_WITH_3DES_EDE_CBC_SHA (0x000a)" \
  "server-ciphersuite" "TLS_RSA_WITH_RC4_128_SHA (0x0005)" \
  "name" "zakir" \
  "cookie" "c_user=100004451022564; datr=ME9yUFtsro9IZo9Bsvx-mEM1; fr=09xG7bUTaV3Praqud.AWUl8VnwVMipiKyhdelnR_ylYXM.BQck9L.mh.AWUmDU8q; lu=Rhm1BbpziSYpwQr9lOfxnanw; xs=61%3ATYLvVr8P4xXmMw%3A0%3A1349668683; sub=3; p=68; wd=1366x643; presence=EM349671297EuserFA21B04451022564A2EstateFDsb2F0Et2F_5b_5dElm2FnullEuct2F1349668084BEtrFA2loadA2EtwF3252494709EatF1349671297352G349671297463CEchFDp_5f1B04451022564F1CC; act=1349671298743%2F4%3A2; _e_0Cjb_4=%5B%220Cjb%22%2C1349671298744%2C%22act%22%2C1349671298743%2C4%2C%22message_body%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fzakirbpd%3Fref%3Dts%26fref%3Dts%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C581%2C393%2C0%2C981%2C16%5D" \
  > "${SOL}"

while read NETID
do
  echo -e "${COUNT}\t${NETID}"
  OUTPUT_DIR="${LOCAL_SVN}/${NETID}"
  if [ ! -d "${OUTPUT_DIR}" ]; then
    continue
  fi
  OUTPUT_DIR="${OUTPUT_DIR}/mp4"
  mkdir "${OUTPUT_DIR}"

  # generate pcap1
  echo "-- generating 4.1.1.pcap"
  MSG_ACTIVE=$(sed -n "${PCAP1_MSG_ACTIVE[${COUNT}]}p" "${MSG_FILE}")
  MSG_PASSIVE=$(sed -n "${PCAP1_MSG_PASSIVE[${COUNT}]}p" "${MSG_FILE}")
  SOL_PCAP1=$(${WORKING_DIR}/scripts/capture_traffic.sh "${PCAP1_SUBNET1[${COUNT}]}" "${PCAP1_SUBNET2[${COUNT}]}" "${MSG_ACTIVE}" "${MSG_PASSIVE}" "${OUTPUT_DIR}" | grep '{"mac":\[')
  echo "\"${NETID}\":${SOL_PCAP1}" >> "${SOL}"

  # generate pcap2
  echo "-- generating 4.1.2.pcap"
  MSG=$(sed -n "${PCAP2_MSG[${COUNT}]}p" "${MSG_FILE}")
  LENGTH=112
  PAD=$(printf '%0.1s' "!"{1..112})
  PADDED_MSG=$(printf '%s%*.*s' "${MSG}" 0 $((LENGTH-${#MSG})) "$PAD" | tr -d '\r')
  echo "\"msg\":\"${PADDED_MSG}\"}," >> "${SOL}"
  MSG=$(xxd -c 112 -l 112 -p <<< "${PADDED_MSG}")
  ${WORKING_DIR}/scripts/mod_pcap2.sh "${MSG}" "scripts/4.1.2.pcap" "${OUTPUT_DIR}"

  chmod 777 ${OUTPUT_DIR}
  chmod 666 ${OUTPUT_DIR}/*
  echo "-- done"
  (( COUNT += 1 ))
done <${ROSTER_FILE}

sed -i '$ s/.$/}/' "${SOL}"
python -m json.tool "${SOL}" > "${WORKING_DIR}/../sol/cp1_sol.json"
rm ${SOL}
rm ${MSG_FILE}

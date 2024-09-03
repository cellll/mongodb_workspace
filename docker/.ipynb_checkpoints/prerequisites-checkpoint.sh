#!/bin/bash
set -a            
source .env
set +a

################################################
########## MAKE DIRECTORY, LOG FILES ###########
################################################

DATA_DIR=${STORAGE_DIR}/data
LOG_DIR=${STORAGE_DIR}/logs

echo "STORAGE DIRECTORY : ${STORAGE_DIR}"
echo "DATA DIRECTORY : ${DATA_DIR}"
echo "LOG DIRECTORY : ${LOG_DIR}"

mkdir -p ${DATA_DIR}/cfgsvr0
mkdir -p ${DATA_DIR}/cfgsvr1
mkdir -p ${DATA_DIR}/cfgsvr2
mkdir -p ${DATA_DIR}/shardsvr00
mkdir -p ${DATA_DIR}/shardsvr01
mkdir -p ${DATA_DIR}/shardsvr02
mkdir -p ${DATA_DIR}/shardsvr10
mkdir -p ${DATA_DIR}/shardsvr11
mkdir -p ${DATA_DIR}/shardsvr12

mkdir -p ${LOG_DIR}
touch ${LOG_DIR}/cfgsvr0.log
touch ${LOG_DIR}/cfgsvr1.log
touch ${LOG_DIR}/cfgsvr2.log
touch ${LOG_DIR}/queryrouter0.log
touch ${LOG_DIR}/shardsvr00.log
touch ${LOG_DIR}/shardsvr01.log
touch ${LOG_DIR}/shardsvr02.log
touch ${LOG_DIR}/shardsvr10.log
touch ${LOG_DIR}/shardsvr11.log
touch ${LOG_DIR}/shardsvr12.log

sleep 1

################################################
############### MAKE CONFIG FILES ##############
################################################

##### CFGSVR
FILEPATH=${CONFIG_DIR}/cfgsvr0.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${CFGSVR0_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${CFGSVR0_IP}/g" ${FILEPATH}

FILEPATH=${CONFIG_DIR}/cfgsvr1.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${CFGSVR1_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${CFGSVR1_IP}/g" ${FILEPATH}

FILEPATH=${CONFIG_DIR}/cfgsvr2.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${CFGSVR2_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${CFGSVR2_IP}/g" ${FILEPATH}

##### QUERYROUTER
FILEPATH=${CONFIG_DIR}/queryrouter0.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${QUERYROUTER0_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${QUERYROUTER0_IP}/g" ${FILEPATH}

TARGET_LINE=$(grep -rn "configDB:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  configDB: ConfigReplSet\/${CFGSVR0_IP}:${CFGSVR0_PORT}/g" ${FILEPATH}

FILEPATH=${CONFIG_DIR}/queryrouter1.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${QUERYROUTER1_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${QUERYROUTER1_IP}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "configDB:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  configDB: ConfigReplSet\/${CFGSVR0_IP}:${CFGSVR0_PORT}/g" ${FILEPATH}


##### SHARDSVR
FILEPATH=${CONFIG_DIR}/shardsvr00.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${SHARDSVR00_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${SHARDSVR00_IP}/g" ${FILEPATH}

FILEPATH=${CONFIG_DIR}/shardsvr01.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${SHARDSVR01_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${SHARDSVR01_IP}/g" ${FILEPATH}

FILEPATH=${CONFIG_DIR}/shardsvr02.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${SHARDSVR02_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${SHARDSVR02_IP}/g" ${FILEPATH}


FILEPATH=${CONFIG_DIR}/shardsvr10.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${SHARDSVR10_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${SHARDSVR10_IP}/g" ${FILEPATH}

FILEPATH=${CONFIG_DIR}/shardsvr11.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${SHARDSVR11_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${SHARDSVR11_IP}/g" ${FILEPATH}

FILEPATH=${CONFIG_DIR}/shardsvr12.conf
TARGET_LINE=$(grep -rn "port:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  port: ${SHARDSVR12_PORT}/g" ${FILEPATH}
TARGET_LINE=$(grep -rn "bindIp:" ${FILEPATH} | cut -d: -f1)
if [ -z ${TARGET_LINE} ]; then echo "TARGET_LINE NOT EXISTS. FILEPATH: ${FILEPATH}"; exit; fi
sed -i "${TARGET_LINE}s/.*/  bindIp: ${SHARDSVR12_IP}/g" ${FILEPATH}


################################################
############# MAKE POSTCONFIG FILE #############
################################################
POST_CONFIG_FILEPATH="post_configs.txt"
cat /dev/null > ${POST_CONFIG_FILEPATH}

echo "1. Setting ConfigServer ReplSet"  >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "docker exec -it mongo_queryrouter0_${CLUSTER_NAME} bash" >> ${POST_CONFIG_FILEPATH}
echo "mongosh ${CFGSVR0_IP}:${CFGSVR0_PORT}" >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "rs.status()" >> ${POST_CONFIG_FILEPATH}
echo "rs.initiate()" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "rs.add(\"${CFGSVR1_IP}:${CFGSVR1_PORT}\")" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "rs.add(\"${CFGSVR2_IP}:${CFGSVR2_PORT}\")" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}

echo "2. Setting ShardServer ReplSet0"  >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "mongosh ${SHARDSVR00_IP}:${SHARDSVR00_PORT}" >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "rs.initiate()" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "rs.add(\"${SHARDSVR01_IP}:${SHARDSVR01_PORT}\")" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "rs.add(\"${SHARDSVR02_IP}:${SHARDSVR02_PORT}\")" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}

echo "3. Setting ShardServer ReplSet1"  >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "mongosh ${SHARDSVR10_IP}:${SHARDSVR10_PORT}" >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "rs.initiate()" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "rs.add(\"${SHARDSVR11_IP}:${SHARDSVR11_PORT}\")" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "rs.add(\"${SHARDSVR12_IP}:${SHARDSVR12_PORT}\")" >> ${POST_CONFIG_FILEPATH}
echo "sleep(500)" >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}

echo "4. Setting sharding"  >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "mongosh ${QUERYROUTER0_IP}:${QUERYROUTER0_PORT}" >> ${POST_CONFIG_FILEPATH}
echo "" >> ${POST_CONFIG_FILEPATH}
echo "sh.addShard(\"ShardReplSet0/${SHARDSVR00_IP}:${SHARDSVR00_PORT}\")"  >> ${POST_CONFIG_FILEPATH}
echo "sh.addShard(\"ShardReplSet1/${SHARDSVR10_IP}:${SHARDSVR10_PORT}\")"  >> ${POST_CONFIG_FILEPATH}


echo "DONE"



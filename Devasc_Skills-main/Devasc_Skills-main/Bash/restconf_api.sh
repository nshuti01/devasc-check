#!/bin/bash

IP_HOST=192.168.56.101
ping -c 3 $IP_HOST 
LOOPBACK_INTERFACE=Loopback199
LOOPBACK_IP=10.1.99.1
USERNAME=cisco
PASSWORD=cisco123!
status_code=$(curl -ks \
-w "%{http_code}" \
-o /dev/null \
-u "$USERNAME:$PASSWORD" \
-H "Accept: application/yang-data+json" \
"https://$IP_HOST/restconf/data/ietf-interfaces:interfaces/interface=$LOOPBACK_INTERFACE"\
"https://$IP_HOST/restconf/data/ietf-interfaces:interfaces")
dt=$(date '+%d/%m/%Y %H:%M:%S')


echo "$dt" > check_restconf_api.txt
echo "START REST API CALL" >> check_restconf_api.txt
echo "===========" >> check_restconf_api.txt
echo "FIRST API CALL" >> check_restconf_api.txt
echo "===========" >> check_restconf_api.txt
echo "$status_code" >> check_restconf_api.txt
echo "SECOND API CALL" >> check_restconf_api.txt
echo "===========" >> check_restconf_api.txt
echo "$status_code" >> check_restconf_api.txt
echo "$Interfaces" >> check_restconf_api.txt
echo "END REST API CALL" >> check_restconf_api.txt

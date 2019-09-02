#!/bin/bash
source /usr/local/greenplum-db/greenplum_path.sh
export MASTER_DATA_DIRECTORY=/data/master/gpseg-1
/etc/zabbix/scripts/greenplum.py

#!/bin/bash
dev=$1
state=$(mdadm --detail ${dev} | grep 'State :' | tr -d ' ' | cut -f 2 -d ':' | cut -f 1 -d ',')
if [[ "${state}" == "clean" || "${state}" == "active" ]]; then
  echo 0 #OK
else
  echo 1 #FAIL
fi

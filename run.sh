#!/bin/sh
WLST=/u01/oracle/oracle_common/common/bin/wlst.sh

echo "Hello from the WebLogic Step"
echo "Reading the config from :" $WERCKER_WEBLOGIC_STEP_CONFIG
cat $WERCKER_WEBLOGIC_STEP_CONFIG

echo "Create domains directory"
mkdir -p /u01/oracle/domains

echo "Checking we can run wlst"
$WLST $WERCKER_STEP_ROOT/test.py

echo "Creating the basic domain"
$WLST $WERCKER_STEP_ROOT/create-domain.py

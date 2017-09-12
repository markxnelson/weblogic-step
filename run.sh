#!/bin/sh
WLST=/u01/oracle/oracle_common/common/bin/wlst.sh

echo "Hello from the WebLogic Step"
echo "Reading the config from :" $WERCKER_WEBLOGIC_STEP_CONFIG
cat $WERCKER_WEBLOGIC_STEP_CONFIG

echo "Checking we can run wlst"
$WLST $WERCKER_ROOT/test.py

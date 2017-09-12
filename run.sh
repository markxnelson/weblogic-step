#!/bin/sh
WLST="/u01/oracle/oracle_common/common/bin/wlst.sh -skipWLSModuleScanning"

echo "Hello from the WebLogic Step"
echo "Reading the config from :" $WERCKER_WEBLOGIC_STEP_CONFIG
cat $WERCKER_WEBLOGIC_STEP_CONFIG

echo "Create domains directory"
mkdir -p /u01/oracle/domains

echo "Create applications directory"
mkdir -p /u01/oracle/applications

echo "Checking we can run wlst"
$WLST $WERCKER_STEP_ROOT/test.py

echo "Creating the basic domain"
$WLST $WERCKER_STEP_ROOT/create-domain.py

echo "Create data sources"
$WLST $WERCKER_STEP_ROOT/create-data-sources.py $WERCKER_WEBLOGIC_STEP_CONFIG

echo "Deploy applications"
$WLST $WERCKER_STEP_ROOT/deploy-applications.py $WERCKER_WEBLOGIC_STEP_CONFIG


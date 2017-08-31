#!/bin/sh
echo "Hello from the WebLogic Step"
# adding a comment
sudo -u oracle DOMAIN_HOME=/u01/oracle/user_projects/domain/base-domain && \
ADMIN_PASSWORD=welcome1 && \
ADMIN_USERNAME=weblogic && \
DOMAIN_NAME=base_domain && \
/u01/oracle/createAndStartEmptyDomain.sh && \
/u01/oracle/oracle_common/common/bin/wlst.sh << EOF
connect ('weblogic', 'welcome1', 't3://localhost:7001')
ls ()
exit() 
EOF


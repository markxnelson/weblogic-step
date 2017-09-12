# create a basic weblogic domain
selectTemplate('Basic WebLogic Server Domain')
loadTemplates()
cd('/Security/base_domain/Users/weblogic')
cmo.setPassword('welcome1')
writeDomain('/u01/oracle/domains/base_domain')
exit()
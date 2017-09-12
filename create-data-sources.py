# create data sources from the config file

import json
import sys

# check a config file was specified
config_file = sys.argv[1]
if (config_file == None):
    raise Error("must specify the config file")
    exit()

# read the config file
data_file = open(config_file, 'r')
data = json.load(data_file)

# look for the data sources
if (data["datasources"] == None):
    print ("No data sources in the config file.. nothing to do")
    exit()

# connect to weblogic
readDomain('/u01/oracle/domains/base_domain')

for datasource in data["datasources"]:

    dsname = datasource["name"]
    dsjndiname = datasource["jndiName"]
    dsurl = datasource["url"]
    dsusername = datasource["user"]
    dspassword = datasource["password"]
    dsdriver = "oracle.jdbc.xa.client.OracleXADataSource"

    print ('Creating Data Source')
    cd('/')
    cmo.createJDBCSystemResource(dsname)

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname)
    cmo.setName(dsname)

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDataSourceParams/' + dsname)
    set('JNDINames',jarray.array([String(dsjndiname)], String))

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDriverParams/' + dsname)
    cmo.setUrl(dsurl)
    cmo.setDriverName(dsdriver)
    set('Password', dspassword)

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCConnectionPoolParams/' + dsname)
    cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n\r\n')
    cmo.setInitialCapacity(0)

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDriverParams/' + dsname + '/Properties/' + dsname)
    cmo.createProperty('user')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDriverParams/' + dsname + '/Properties/' + dsname + '/Properties/user')
    cmo.setValue(dsusername)

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDataSourceParams/' + dsname)
    cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

    print ('Targeting DS to the AdminServer')

    cd ('/JDBCSystemResources/'+ dsname)
    set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

# disconnect

updateDomain()
closeDomain()
exit()
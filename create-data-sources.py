# create data sources from the config file

import sys

# check a config file was specified
config_file = sys.argv[1]
if (config_file == None):
    raise Error("must specify the config file")
    exit()

# read the config file
data_file = open(config_file, 'r')
data = eval(data_file.read())

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
    create(dsname, 'JDBCSystemResource')
    set('Target','AdminServer')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname)
    cmo.setName(dsname)

    create('myJdbcDataSourceParams','JDBCDataSourceParams')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDataSourceParams/NO_NAME_0')
    set('JNDIName',[String(dsjndiname)], String)
    set('GlobalTransactionsProtocol', 'TwoPhaseCommit')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname)
    create('myJdbcDriverParams','JDBCDriverParams')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDriverParams/NO_NAME_0')
    set('URL', dsurl)
    set('DriverName', dsdriver)
    set('PasswordEncrypted', dspassword)

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname)
    create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCConnectionPoolParams/NO_NAME_0')
    set('TestTableName', 'SQL SELECT 1 FROM DUAL')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname)
    create('myProperties','Properties')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/Properties/NO_NAME_0')
    create('user', 'Property')

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/Properties/NO_NAME_0/Properties/user')
    set('Value', dsusername)

    cd('/JDBCSystemResources/' + dsname + '/JDBCResource/' + dsname + '/JDBCDataSourceParams/' + dsname)

# disconnect

updateDomain()
closeDomain()
exit()



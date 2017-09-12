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
    cd('/JDBCSystemResources/' + dsname)
    set('Target','AdminServer')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname)
    cmo.setName(dsname)

    create('myJdbcDataSourceParams','JDBCDataSourceParams')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname + '/JDBCDataSourceParams/NO_NAME_0')
    set('JNDIName', dsjndiname)
    set('GlobalTransactionsProtocol', 'TwoPhaseCommit')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname)
    create('myJdbcDriverParams','JDBCDriverParams')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname + '/JDBCDriverParams/NO_NAME_0')
    set('URL', dsurl)
    set('DriverName', dsdriver)
    set('PasswordEncrypted', dspassword)

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname)
    create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname + '/JDBCConnectionPoolParams/NO_NAME_0')
    set('TestTableName', 'SQL SELECT 1 FROM DUAL')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname + '/JDBCDriverParams/NO_NAME_0')
    create('myProperties','Properties')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname + '/JDBCDriverParams/NO_NAME_0/Properties/NO_NAME_0')
    create('user', 'Property')

    cd('/JDBCSystemResources/' + dsname + '/JdbcResource/' + dsname + '/JDBCDriverParams/NO_NAME_0/Properties/NO_NAME_0/Property/user')
    set('Value', dsusername)

# disconnect

updateDomain()
closeDomain()
exit()



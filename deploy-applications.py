# deploy applications from the config file

import sys

# check a config file was specified
config_file = sys.argv[1]
if (config_file == None):
    raise Error("must specify the config file")
    exit()

# read the config file
data_file = open(config_file, 'r')
data = eval(data_file.read())

# look for the deployments
if (data["deployments"] == None):
    print ("No deployments in the config file.. nothing to do")
    exit()

# connect to weblogic
readDomain('/u01/oracle/domains/base_domain')

for deployment in data["deployments"]:

    appname = deployment["name"]
    apppkg = deployment["source"]
    appdir = '/u01/oracle/applications'

    cd('/')
    app = create(appname, 'AppDeployment')
    app.setSourcePath(appdir + '/' + apppkg)
    app.setStagingMode('nostage')

    # Assign application to AdminServer
    # =================================
    assign('AppDeployment', appname, 'Target', 'AdminServer')

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
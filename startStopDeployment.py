from java.io import FileInputStream



def startDeployment(appName):
  
  print '\n--- Start Deployment: ' + appName + ' --\n'
  startApplication(appName)
  print '==================================\n'
  

def stopDeployment(appName):

  print '\n--- Stop Deployment: ' + appName + ' --\n'
  stopApplication(appName)
  print '=================================\n'


def main():
  propInputStream = FileInputStream(sys.argv[1])
  configProps = Properties()
  configProps.load(propInputStream)
   
  url=configProps.get("adminUrl")
  username=configProps.get("importUser")
  password=configProps.get("importPassword")
  apps=configProps.get("apps")
  
  connect(username , password , url)
  
  app=apps.split(',')
  
  for i in app:
    appName = i.split('|')[0]
    appAction = i.split('|')[1]
	
    if appAction == 'start':
      startDeployment(appName)
    elif appAction == 'stop':
      stopDeployment(appName)
    else:
      print '!!! ERROR !!!'
      print 'Wrong input action parameter: (start|stop)'
      exit(exitcode=101)
	
	
  disconnect()

main()
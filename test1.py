from MySQLModel import *
from WarningModel import *

dbobj=mysqlDB()
s=dbobj.querydb()
computers=[]

for ss in s:
    computers.append(Computer(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6]))
print(s)
print(computers[0].id,computers[0].model,computers[0].address,computers[0].owneremail,computers[0].ownername,computers[0].ownerphone,computers[0].ip)
print(computers[0].model)


dbobj.updatedb(computers[0].id,36.1,'25%')
s2=dbobj.querytemp(computers[0].id)
s1=dbobj.querydb()
s3=dbobj.queryload(computers[0].id)
print(s1)
print(s2)
print(s3)

# testemail=computers[0].owneremail
# warningsend("Lenovo","江苏南通","谢骏鑫","junxinxie360@gmail.com")

dbobj.closedb()
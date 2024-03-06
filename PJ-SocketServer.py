# 具体落实到项目上的信息传输系统的服务端代码
# 首先我们要做的是 使用自己编写的MySQLModel模块 从部署的Django网站获取要监控的机器信息

# 在这之前，项目会先运行Django网站，收集数据
from MySQLModel import *

# 从模块中实例化一个对象来进行此类的相关操作
dbobj = mysqlDB()
# 查询已经在网站上注册过的机器数据
datas = dbobj.querydb()
# 列表存放
computers = []
# 统计要求监测的计算机台数
cnt = 0

# 利用字典实现待监测计算机和id号的信息绑定 用注册的机器的ip实现绑定 唯一的
# 创建一个空字典
iptoid = dict()

for data in datas:
    # 对应的读取的数据依次是
    # id,ip,model,address,ownername,ownerphone,owneremail
    computers.append(Computer(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    # ip绑定id(这里之间映射到这个computer类对象上面) 便于数据的更新 ip是用户输入的信息所保证的
    iptoid[data[1]] = Computer(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    cnt += 1

# 统计的电脑台数是为了后续如果进行优化后线程设计所采取的举措
# 此外,id是进行单台电脑和数据库的联系 便于收取的温度等信息进行动态更新
# model,address,ownername,ownerphone,owneremail是用来发送报警信息的关键数据信息
# ip是进行socket通信的关键数据信息

# 进行多线程socket通信的模块
from socket import *
from threading import Thread

IP = ''
# 7729是云服务器部署开放的专门用于此项目的端口号
PORT = 7729
BUFLEN = 1024

from WarningModel import *
# 这是新线程执行的函数，每个线程负责和一个客户端进行通信
def clientHandler(dataSocket, addr):
    while True:
        recved = dataSocket.recv(BUFLEN)
        # 客户端不发生数据时 认为关闭了连接
        if not recved:
            break

        # 字符串解码
        # 发送的数据应该是监测到的主机的温度和负载信息
        # 我们规则化这样的信息发送格式为一串字符串 然后采用“发送的客户端ip 温度 负载”的格式
        # info 利用split方法切割后是一个长度为3的字符串序列
        info = (recved.decode()).split()
        tip = info[0]
        tobj=iptoid[tip]
        ttemperature = float(info[1])
        tloads = info[2]
        tid = tobj.id
        tmodel=tobj.model
        taddr=tobj.address
        townername=tobj.ownername
        towneremail=tobj.owneremail
        
        #输出信息提示更加清晰
        print(f'收到IP地址为{tip}的客户端发送过来的温度和负载信息:{ttemperature} {tloads}')

        dataSocket.send(f'服务端收到了温度和负载信息:{ttemperature} {tloads}'.encode())

        # 接下来便可以利用数据库模块进行数据库交互了
        dbobj.updatedb(tid, ttemperature, tloads)
        # 这样便在服务器端收到了监测信息并且和数据库交互实现了实时的更新 在Django web端也可实时动态查看更新的数据

        #这里还有一个报警功能需要实现
        #我们设定报警的CPU温度阈值是91摄氏度
        if ttemperature>91.0:
            warningsend(tmodel,taddr,townername,towneremail)

    dataSocket.close()


listenSocket = socket(AF_INET, SOCK_STREAM)
listenSocket.bind((IP, PORT))
listenSocket.listen(128)

# 循环接收客户端的请求
while True:
    dataSocket, addr = listenSocket.accept()
    print(f'成功与IP地址及端口号为{addr}建立连接!')
    addr = str(addr)

    # 成功连接一个客户端请求后创建一个新的线程来处理这样一个连接
    th = Thread(target=clientHandler, args=(dataSocket, addr))
    # 启动子线程
    th.start()

listenSocket.close()
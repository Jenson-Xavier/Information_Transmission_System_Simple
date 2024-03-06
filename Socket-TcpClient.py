#python 一个TCP socket通信代码模板框架
from socket import *

#绑定服务器连接套接字 这里用云服务器的套接字
IP='101.43.71.22'
SERVER_PORT=7729
BUFLEN=1024

#实例化一个socket对象
dataSocket=socket(AF_INET,SOCK_STREAM)

#连接服务端socket
dataSocket.connect((IP,SERVER_PORT))

while True:
    #先从终端用户输入字符串作为通信的消息
    toSend=input('>>> ')
    if toSend == 'exit':
        break
    #信息的编码
    dataSocket.send(toSend.encode())

    #等待接收服务端的消息
    recved=dataSocket.recv(BUFLEN)
    #如果返回空bytes,表示对方关闭了连接
    if not recved:
        break
    #打印读取的信息
    print(recved.decode())

dataSocket.close()

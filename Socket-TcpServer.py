#python 一个TCP socket通信代码模板框架
from socket import *

#主机地址为空字符串,标识绑定本机所有网络接口ip地址
#等待客户端来连接
IP=''
#部署到云服务器开的防火墙用来socket通信
PORT=7729
#定义一次从socket缓冲区最多读入的字节数据
BUFLEN=1024

#实例化一个socket对象
#参数 AF_INET 表示该socket网络层使用IP协议
#参数 SOCK_STREAM 表示该socket传输层使用TCP协议
listenSocket=socket(AF_INET,SOCK_STREAM)

#socket绑定地址和端口
listenSocket.bind((IP,PORT))

#使socket处于监听状态,等待客户端的连接请求
#参数 8 表示 最多接受多少个等待连接的客户端
listenSocket.listen(8)

#从客户端接收到的连接
dataSocket,addr=listenSocket.accept()

while True:
    #从缓冲区里最多读取字节数
    recved=dataSocket.recv(BUFLEN)

    #如果返回空bytes,表示对方关闭了连接
    #退出循环,结束消息收发
    if not recved:
        break

    #要注意读取的字节数据是bytes类型,需要解码为字符串
    info=recved.decode()
    print(f'收到客户端信息:{info}')

    #回送数据必须也是bytes,故需要编码
    dataSocket.send(f'服务端收到了信息 {info}'.encode())

#Socket调用close()关闭
dataSocket.close()
listenSocket.close()
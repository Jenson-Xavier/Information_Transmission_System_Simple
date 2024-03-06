#项目数据库交互模块

#创建一个全局computers列表用来存储每个类实例化对象
computers=[]

#创建一个基类表示computer的一些属性 用来存储计算机的相关信息
class Computer:
    id=0
    ip='0.0.0.0'
    model='null'
    address='null'
    ownername='null'
    ownerphone='***********'
    owneremail='*********@**.***'

    #类实例化构造函数
    def __init__(self,id,ip,model,address,ownername,ownerphone,owneremail):
        self.id=id
        self.ip=ip
        self.model=model
        self.address=address
        self.ownername=ownername
        self.ownerphone=ownerphone
        self.owneremail=owneremail

#这个类设计仅仅是用来存放computer的相关信息的 它不考虑类方法设计

import pymysql

#查询数据库获得信息函数 增加删除改动均在Djangoweb界面完成
def getComputer():
    #连接数据库
    con=pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='xjx20030126',
                               port=3306,
                               db='test',
                               charset='utf8')

    cur=con.cursor()
    sql='select * from myapp_computer'
    #执行查找
    try:
        cur.execute(sql)
        computersIN=cur.fetchall()
        return computersIN
    except:
        con.rollback()
    #关闭数据库
    cur.close()
    con.close()

#更新数据库 服务器端根据获得的温度信息实时跟新数据库
def updateComputer(id,temperature,loads):
    con = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='xjx20030126',
                                 port=3306,
                                 db='test',
                                 charset='utf8')
    cur=con.cursor()
    sql="update myapp_computer set temperature=%f,loads='%s' where id=%d" % (temperature,loads,id)
    try:
        cur.execute(sql)
        con.commit()
    except:
        con.rollback()
    cur.close()
    con.close()


#考虑到数据库交互操作在驻留程序中是实时更新的 也就是说更新数据库操作是非常频繁的 我们可以利用全局变量 专门设计打开和关闭数据库的函数 类封装实现
class mysqlDB:
    def __init__(self):
        try:
            self.connection=pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='xjx20030126',
                                 port=3306,
                                 db='test',
                                 charset='utf8')
            self.cursor=self.connection.cursor()
        except:
            print('数据库连接失败！')

    def closedb(self):
        self.cursor.close()
        self.connection.close()

    def querydb(self):
        sql='select * from myapp_computer'
        try:
            self.cursor.execute(sql)
            information=self.cursor.fetchall()
            return information
        except:
            self.connection.rollback()
            print('查找数据库信息失败！')

    def querytemp(self,id):
        sql='select temperature from myapp_computer where id=%d' % id
        try:
            self.cursor.execute(sql)
            information=self.cursor.fetchone()
            return information[0]
        except:
            self.connection.rollback()
            print('查找数据库温度信息失败！')

    def queryload(self,id):
        sql='select loads from myapp_computer where id=%d' % id
        try:
            self.cursor.execute(sql)
            information=self.cursor.fetchone()
            return information[0]
        except:
            self.connection.rollback()
            print('查找数据库负载信息失败！')

    def updatedb(self,id,temperature,loads):
        sql = "update myapp_computer set temperature=%f,loads='%s' where id=%d" % (temperature, loads, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except:
            self.connection.rollback()
            print('数据库信息更新失败！')
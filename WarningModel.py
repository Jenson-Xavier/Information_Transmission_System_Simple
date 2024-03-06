#暂定模块操作为邮件提醒 使用我们的qq作为发送方 当然也可以重新注册一个邮箱 这里暂时先用qq测试
import yagmail
def warningsend(model,address,ownername,email):
    try:
        yag=yagmail.SMTP(user='1833610970@qq.com',password='ijompckmwesihbbf',host='smtp.qq.com')
        content=f'Hello,{ownername}!Your {model} computer in {address} or other devices now have high CPU temperatures or CPU loads! Attention!!'
        yag.send(to=email,subject='Warning',contents=content)
    except:
        print('Send Failure!')

#结合多线程测试情况可以发现一个小的问题
#我们是能够实现多线程多个客户端的访问 测试效果也是正常的 但是由于测试的时候我们并没有实际的监控程序
#为了测试功能 我们选择了认为持续发送报警数据 这样每个线程均会调用报警信息发送函数
#于是我们注意到 当两个或者多个客户端同时运行一段时候后 出现了Send Failure问题 就是因为频繁发送邮件并且在极短的时间冲突下
#用的是同一个QQ邮件服务器作为发送放还没有完整地发出一封就被调用发来另一封
#实际应用中出现CPU过载的情况并非频繁的 且多个客户端的访问也只有极小的概率会出现这样的碰撞现象 而且我们也可以通过巧妙地设置slepp时长来优化
#在此记录一下存在的小问题和不完善之处
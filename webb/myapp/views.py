from collections import UserList
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse
from django.http import HttpResponse
from myapp.models import Computer
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.

#浏览主界面
def users(request):
    try:
        Userslist = Computer.objects.filter(host_id = request.user.id)
        context = {"userslist": Userslist}
        return render(request, 'myapp/users.html', context)
    except:
        return render(request, 'myapp/users.html')

#添加界面
def AddUsers(request):
    return render(request, "myapp/add.html")

#添加执行
def InsertUsers(request):
    try:
        ob = Computer()
        ob.ip = request.POST['ip']
        ob.address= request.POST['address']
        ob.ownername= request.POST['ownername']
        ob.ownerphone= request.POST['ownerphone']
        ob.owneremail= request.POST['owneremail']
        ob.model = request.POST['model']
        ob.host = User.objects.get(id=request.user.id)
        ob.save()
        context  = {"info": "添加成功"}
    except:
        context  = {"info": "添加失败"}
    return render(request, 'myapp/info.html', context)

#删除
def DelUsers(request, uid = 0):
    try:
        ob = Computer.objects.get(id = uid)
        ob.delete()
        context  = {"info": "删除成功"}
    except:
        context =  {"info": "删除失败"}
    return render(request, 'myapp/info.html', context)

#服务器信息编辑界面
def EditUsers(request, uid = 0):
    try:
        ob = Computer.objects.get(id = uid)
        context = {"user": ob}
        return render(request, "myapp/edit.html", context)
    except:
        context = {"info": "编辑加载失败"}
        return render(request, "myapp/info.html", context)

#服务器信息编辑执行
def UpdateUsers(request):
    try:
        upid = request.POST['id']
        ob = Computer.objects.get(id = upid)
        ob.ip = request.POST['ip']
        ob.address= request.POST['address']
        ob.ownername= request.POST['ownername']
        ob.ownerphone= request.POST['ownerphone']
        ob.owneremail= request.POST['owneremail']
        ob.model = request.POST['model']
        ob.save()
        context = {"info": "修改成功"}
    except:
        context = {"info": "修改失败"}
    return render(request, 'myapp/info.html', context)

def page_not_found(request, exception):
    
    return redirect('myapp:users')


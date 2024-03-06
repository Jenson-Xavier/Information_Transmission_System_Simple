from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm

# Create your views here.

#注册账号
def register(request):
    return render(request, 'myapp/register.html')

#忘记密码
def forgetpass(request):
    return render(request, 'myapp/forgetpass.html')

#登出账号方法
def user_logout(request):
    logout(request)
    return redirect('userprofile:login')

#登录账号
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
             # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(request,username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect('myapp:users')
            else:
                context = {'errorinfo': "账号不存在或密码错误"}
                return render(request, 'userprofile/login.html', context)
        else:
            return HttpResponse("输入数据不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        return render(request, 'userprofile/login.html')
    else:
        return HttpResponse('请使用GET或POST请求')
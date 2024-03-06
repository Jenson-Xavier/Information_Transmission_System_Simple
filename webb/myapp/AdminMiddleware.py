#from importlib.resources import path
from django.shortcuts import render
from django.http import HttpResponse, request, response
from django.shortcuts import redirect
from django.urls import reverse
import re

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        path = request.path
        # print(path)调试用代码，输出当前的url
        if re.match('^/computers', path):
            if not request.user.is_authenticated:
                return redirect('userprofile:login')
        response = self.get_response(request)
        
        return response
from django.urls import path, reverse
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('', views.user_login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('forgetpass', views.forgetpass, name = 'forgetpass'),
    path('logout', views.user_logout, name = 'logout'),
]
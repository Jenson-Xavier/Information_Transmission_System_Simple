from django.urls import path, reverse
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.users, name = 'users'),
    path('add', views.AddUsers,name="addusers"),
    path('insert', views.InsertUsers,name="insertusers"),
    path('del/<int:uid>', views.DelUsers,name="delusers"),
    path('edit/<int:uid>', views.EditUsers,name="editusers"),
    path('update', views.UpdateUsers,name="updateusers"),
]
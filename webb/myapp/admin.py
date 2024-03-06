from django.contrib import admin

# Register your models here.
# 别忘了导入ArticlerPost
from .models import Computer

# 注册ArticlePost到admin中
admin.site.register(Computer)
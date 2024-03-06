from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Computer(models.Model):
    ip=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    ownername=models.CharField(max_length=30)
    ownerphone=models.CharField(max_length=30)
    owneremail=models.CharField(max_length=30)
    temperature=models.FloatField(default=0)
    loads=models.CharField(max_length=30)
    host=models.ForeignKey(User, on_delete=models.CASCADE)



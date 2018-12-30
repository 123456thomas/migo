from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """定义了一个用户扩展数据类型，要和系统内置的用户一对一关联"""
    id = models.AutoField(primary_key=True)
    header = models.ImageField(upload_to='static/images/headers/',
                               default='static/images/headers/default.png')
    nickname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.InterrField(default=0)
    gender = models.CharField(max_length=5)

    # 和系统内置的用户关联
    user = models.OneToOneField(User, on_delete=models.CASCADE)
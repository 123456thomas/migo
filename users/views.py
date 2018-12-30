from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html',{})
    elif request.method == 'POST':
        # 获取用户数据
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']

        # 判断数据是否可用
        try:
            user = User.objects.get(username=username)
            return render(request, 'users/register.html',
                          {'error_code': -1, 'error_msg': '该账号已经存在，请使用其它账号注册'})
        except:
            # 判断昵称是否可用
            try:
                user_profile = User.userprofile.objects.get(nicjname=nickname)
                return render(request,'users/register.html',
                            {'error_code':-2,'error_msg':'该昵称已经存在，请使用其它昵称'})
            except:
                user = User.objects.create_user(username=username, password=password)
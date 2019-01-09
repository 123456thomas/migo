from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# authenticate:身份认证(判断账号、密码是否正确)；login:登陆并记录登陆状态；logout:销毁登陆状态
from django.contrib.auth import authenticate, login, logout
from . import models
# Create your views here.

# 注册
def users_register(request):
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
                userprofile = models.UserProfile(nickname=nickname, user=user)
                user.save()
                userprofile.save()
                return redirect('users:users_login')

#
# def users_login(request):
#     if request.method == 'GET':
#         # 登陆成功后跳转到下一个页面
#         return render(request, 'users/login.html',{})
#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # 判断验证登陆
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 # 记录登陆状态,跳转页面
#                 return redirect(reverse('commen:index'))
#             else:
#                 return render(request, 'users/login.html', {'error_code': -2, 'error_msg': '账号被锁定，请联系管理员'})
#
#         else:
#             return render(request, 'users/login.html', {'error_code': -1, 'error_msg': '账号或密码有误，请重新输入'})


def users_login(request):
    if request.method == 'GET':
        # 登陆成功后跳转到下一个页面
        try:
            next_url = request.GET['next']
        except:
            next_url = '/'
        return render(request, 'users/login.html',{'next_url': next_url})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST['next_url']
        # 判断验证登陆
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # 记录登陆状态,跳转页面
                # return redirect(reverse('commen:index'))
                # 将user给request
                login(request, user)
                print(next_url)
                return redirect(next_url)
            else:
                return render(request, 'users/login.html', {'error_code': -2, 'error_msg': '账号被锁定，请联系管理员'})

        else:
            return render(request, 'users/login.html', {'error_code': -1, 'error_msg': '账号或密码有误，请重新输入'})


def users_logout(request):
    """用户退出登陆"""
    logout(request)
    return render(request, 'commen/index.html', {'error_code': 1, 'error_msg': '账号成功退出'})

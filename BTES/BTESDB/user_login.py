from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单
from django.contrib.auth.models import User   #导入django自带的user表
from django.utils import timezone

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (str(username)+'    '+str(password))
        re = auth.authenticate(username=username,password=password)  #用户认证
        if re is not None:  #如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
            this_user=User_Info.objects.get(username=username)
            request.session['username']=username
            print (request.session['username'])
            if this_user.is_active==True:
                auth.login(request,re)   #登陆成功
                this_user.login_amount+=1
                this_user.last_login=timezone.now()
                this_user.save()                               
                return redirect('/',{'user':re})    #跳转--redirect指从一个旧的url转到一个新的url
            else:
                return render(request,'login.html',{'login_error':'您的账号申请还在审核中'})  #登陆失败
        else:  #数据库里不存在与之对应的数据
            return render(request,'login.html',{'login_error':'用户名或密码错误'})  #登陆失败
    return render(request,'login.html')
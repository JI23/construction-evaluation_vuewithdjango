from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单
from django.contrib.auth.models import User   #导入django自带的user表
from django.utils import timezone
from django.http import JsonResponse
def login(request):
    if request.method == 'GET':
        response={}
        username = request.GET['username']
        password = request.GET['password']
        print (str(username)+'    '+str(password))
        re = auth.authenticate(username=username,password=password)  #用户认证
        
        #如果这里想改成从用户信息表中判断是否存在 
        #user_exist=User_Info.objects.filter(username=username,password=password)
        #if user_exist.exists():
        
        if re is not None:  #如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
            print (1)
            this_user=User_Info.objects.get(username=username)
            #request.session['username']=username
            #print (request.session['username'])
            response['username']=username
            response['password']=password
            if  this_user.is_staff==True:#登陆成功
                print(2)
                response['error_num']=0
                response['msg']='success'
                auth.login(request,re)   
                this_user.login_amount+=1
                this_user.last_login=timezone.now()
                this_user.save() 
                response['admin'] = this_user.is_superuser
                return JsonResponse(response)                              
            else:
                print ('未审核')
                response['error_num']=1
                response['msg']='failed'
                return JsonResponse(response)
        else:  #数据库里不存在与之对应的数据
            print(3)
            response['error_num']=2
            response['msg']='failed'
            return JsonResponse(response)
    return JsonResponse(response)
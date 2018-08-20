from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from BTESDB.models import Project,User_Info
from django.contrib import auth
#from django import forms    #导入表单
#from django.contrib.auth.models import User   #导入django自带的user表
#from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt
#def step1(request):
    #render(request,'step1.vue')

def step1(request):
    print(1)
    response={}
    #username=request.session['username']
    #获取表单数据
    try:
        print(2)
        project_name=request.GET['project_name']
        client_name=request.GET['client_name']
        project_description=request.GET['project_description']
        project_leader=request.GET['project_leader']
        #username=request.GET['username']
        this_user=User_Info.objects.get(username='13051997327')
        if len(project_name)==0:
            response['msg']='项目名称不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        elif Project.objects.filter(user=this_user,project_name=project_name).exists():
            response['msg']='项目名称不得重复！'
            response['error_num']=1
            return JsonResponse(response)
        
        if len(client_name)==0:
            response['msg']='客户名称不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        if len(project_leader)==0:
            response['msg']='项目负责人不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        if len(project_description)==0:
            response['msg']='项目描述不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        
        #获取user外键
        #this_user=User_Info.objects.get(username='13051997327')

        response['error_num']=0
        response['msg']='success'
        response['project_name']=project_name
        response['client_name']=client_name
        response['project_leader']=project_leader
        response['project_description']=project_description
        print(3)
        
    except Exception as e:
        print (4)    
        response['msg']=str(e)
        response['error_num']= 1
    return JsonResponse(response)
        
 
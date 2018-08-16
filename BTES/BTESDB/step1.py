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
            

        #获取user外键
        #this_user=User_Info.objects.get(username='13051997327')
        '''    
        request.session['project_name']=project_name
        request.session['client_name']=client_name
        request.session['project_description']=project_description
        request.session['project_leader']=project_leader
        print(request.session['project_name'])
        '''
        response['error_num']=0
        response['msg']='success'
        response['project_name']=project_name
        response['client_name']=client_name
        response['project_leader']=project_leader
        response['project_description']=project_description
        print(3)
        #print (username)
        #return HttpResponse('<p>数据添加成功</p>')
    except Exception as e:
        print (4)
        response['msg']=str(e)
        response['error_num']=1
    finally:
        #print (list(request.session.keys()))
        return JsonResponse(response)
        
 
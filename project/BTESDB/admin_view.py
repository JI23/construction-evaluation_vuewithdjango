# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Project,User_Info,DB_part,DB_template,Company_Info
from django.contrib import auth
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def show_projects_filter(request):
    '''展示所有项目，所有已完成项目'''
    response = {}
    try:
        condition=request.GET['condition']
        if condition=='all':
            projects = Project.objects.all() 
        elif condition=='finish':
            projects=Project.objects.filter(is_finished=True)
        response['projects']  = json.loads(serializers.serialize("json", projects))
        response['msg'] = 'success'
        response['error_num'] = 0
        #print (response)
    except  Exception as e:
        print (str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_users_all(request):
    response = {}
    try:
        users = User_Info.objects.all()         
        response['users']  = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
        #print (response)
    except  Exception as e:
        print (str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_user_projects(request):
    '''展示特定用户的项目'''
    response = {}
    try:
        username=request.GET['username']
        this_user=User_Info.objects.get(username=username)
        projects = Project.objects.filter(user=this_user)         
        response['projects']  = json.loads(serializers.serialize("json", projects))
        response['msg'] = 'success'
        response['error_num'] = 0
        #print (response)
    except  Exception as e:
        print (str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def allow_user(request):
    '''通过用户申请'''
    response = {}
    try:
        username=request.GET['username']
        this_user=User_Info.objects.get(username=username)
        this_user.is_staff=True
        response['msg']='成功通过用户申请'
        response['error_num']=0
    except Exception as e:
        print (str(e))
        response['msg'] = str(e)
        response['error_num']=1
    return JsonResponse(response)

def refuse_user(request):
    '''对is_staff=False的用户拒绝，执行删除操作'''
    response={}
    try:
        username=request.GET['username']
        User_Info.objects.get(username=username).delete()
        response['msg']='成功拒绝用户申请'
        response['error_num']=0
    except Exception as e:
        print(str(e))
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)

def ban_user(request):
    '''禁用用户'''
    response = {}
    try:
        username=request.GET['username']
        this_user=User_Info.objects.get(username=username)
        this_user.is_staff=False
        response['msg']='成功禁用用户'
        response['error_num']=0
    except Exception as e:
        print (str(e))
        response['msg'] = str(e)
        response['error_num']=1
    return JsonResponse(response)

def filter_user(request):
    '''正常/禁用/待审核的用户'''
    response={}
    try:
        flag=request.GET['flag']
        users=0
        if flag=='0':
            users=User_Info.objects.filter(is_staff=False)
        elif flag=='1':
            users=User_Info.objects.filter(is_staff=True)
        elif flag=='2':
            users=User_Info.objects.filter(is_staff=False,project=0)        
        response['users']=json.loads(serializers.serialize("json", users))
        response['msg']='success'
        response['error_num']=0
    except Exception as e:
        print (str(e))
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)

from itertools import chain
def search_user(request):
    response={}
    try:
        search_condition=request.GET['search_condition']
        users1=User_Info.objects.filter(truename__contains=search_condition)
        users2=User_Info.objects.filter(telephone__contains=search_condition)
        users3=User_Info.objects.filter(architect_id__contains=search_condition)
        #可能会出现重复的元素
        users=chain(users1,users2,users3)
        response['users']=json.loads(serializers.serialize("json", users))
        response['msg']='success'
        response['error_num']=0
    except Exception as e:
        print (str(e))
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)

def admin_index(request):
    '''主页'''
    response={}
    try:
        people_sum=User_Info.objects.filter(is_staff=True).count()
        company_sum=Company_Info.objects.all().count()
        project_sum=Project.objects.all().count()
        project_finish=Project.objects.filter(is_finished=True).count()
        response['people_sum']=people_sum
        response['company_sum']=company_sum
        response['project_sum']=project_sum
        response['project_finish']=project_finish
        response['msg']='全部查找到'
        response['error_num']=0
    except Exception as e:
        print(str(e))
        response['error_num']=1
        response['msg']=str(e)
    return JsonResponse(response)





# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Project
from django.contrib import auth
from django import forms    #导入表单
from django.contrib.auth.models import User   #导入django自带的user表
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    #主页
    try:
        username=request.session['username']
        this_user=User_Info.objects.get(username=username)
        project_list=Project.objects.filter(user=this_user)
    except Exception:
        print('还没登陆')
    finally:
        return render(request,'index.html',locals())

def logout(request):
    #登出
    auth.logout(request)
    return render(request,'index.html')
@csrf_exempt
def show_projects(request):
    response = {}
    try:
        #projects = Project.objects.filter(is_finished=is_finished)
        projects = Project.objects.all()
        print (1)
        id=request.POST.get['id']
        print (request.body+'111111')
        print (id)
        response['list']  = json.loads(serializers.serialize("json", projects))
        response['msg'] = 'success'
        response['error_num'] = 0
        #print (response)
    except  Exception as e:
        print (2)
        response['msg'] = str(e)
        response['error_num'] = 1
    print (3)
    return JsonResponse(response)
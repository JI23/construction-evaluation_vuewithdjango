# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Project,User_Info,DB_part,DB_template
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


@csrf_exempt
def show_projects_all(request):
    response = {}
    try:
        projects = Project.objects.all()         
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

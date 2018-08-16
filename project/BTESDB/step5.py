from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from BTESDB.models import Earthquake_Info,Project,Earthquake_wave_detail
from django.core import serializers
import requests
import json
def step5(request):
    #获取指向该项目的对象
    project=request.GET['project']
    this_project=Project.objects.get(id=project)
    response={}
    try:
        print(2)
        print (request.GET)
        #获取数据
        defense_intensity=request.GET['defense_intensity']
        site_type=request.GET['site_type']
        number=request.GET['number']       
        group=request.GET['group']
        earthquake_level=request.GET['earthquake_level']
        print(3)
        #存入数据库
        new=Earthquake_Info(project=this_project,
        defense_intensity=defense_intensity,
        site_type=site_type,
        number=number,
        group=group,
        earthquake_level=earthquake_level)
        new.save()

        print(4)
        response['msg']='success'
        response['error_num']=0
    except Exception as e:
        response['msg']=str (e)
        response['error_num']=1
    
    return JsonResponse(response)

import ast
def save_waves(request):
    print(1)
    response={}
    #获得指向project的对象
    project=request.GET['project']
    this_project=Project.objects.get(id=project)
    print(2)
    #获取表单内容
    wave_list=request.GET.getlist('earthquake_info[]',[])
    print(3)
    print(wave_list)
    for item in wave_list:
        print(4)
        print (item)
        print (type(item))
        a=ast.literal_eval(item)
        try:
            new=Earthquake_wave_detail(
                project=this_project,
                earthquake_wave_no=a['earthquake_no'],
                earthquake_wave_name=a['name'],
                peak=a['peak'],
                earthquake_wave_file=a['file']
            )
            new.save()
            response['msg']='success'
            response['error_num']=0
        except Exception as e:
            print(str(e))
            response['msg']=str(e)
            response['error_num']=1
    return JsonResponse(response)



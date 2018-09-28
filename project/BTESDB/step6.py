from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from BTESDB.models import Project,Structure_response
from django.core import serializers
import requests
import json

import ast
def step6(request):
    response={}
    try:       
        #获取数据
        project=request.GET['project']
        data_list=request.GET.getlist('data[]',[])
    except Exception:
        response['msg']='请完整填写结构响应信息！'
        response['error_num']=1
        return JsonResponse(response)
    #获取指向该项目的对象
    this_project=Project.objects.get(id=project)
    for item in data_list:
        #将string转化为dict
        a=ast.literal_eval(item)
        if Structure_response.objects.filter(project=this_project,direction=a['direction']).exists():
            #更新数据库中内容
            update=Structure_response.objects.get(project=this_project,direction=a['direction']) 
            update.EDP_type=a['EDP_type']
            update.floor_no=a['floor_no']
            update.earthquake_no=a['earthquake_no']
            update.data=data_list
            update.save()
            response['msg']='结构响应信息修改成功'
            response['error_num']=0
        else:
            #新增数据库中内容
            new=Structure_response(
                project=this_project,
                direction=a['direction'],
                EDP_type=a['EDP_type'],
                floor_no=a['floor_no'],
                earthquake_no=a['earthquake_no'],
                data=data_list)
            new.save()
            response['msg']='结构响应信息新增成功'
            response['error_num']=0
    return JsonResponse(response)

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from BTESDB.models import Project,Structure_response
from django.core import serializers
import requests
import json

import ast
def step6(request):
    #获取指向该项目的对象
    project=request.GET['project']
    this_project=Project.objects.get(id=project)
    response={}
    try:
        print(2)
        print (request.GET)
        #获取数据
        data_list=request.GET.getlist('data[]',[])
        for item in data_list:
            print (item)
            print (type(item))

            a=ast.literal_eval(item)
            print(3)
            new=Structure_response(
                project=this_project,
                direction=a['direction'],
                EDP_type=a['EDP_type'],
                floor_no=a['floor_no'],
                earthquake_no=a['earthquake_no']
            )
            new.save()
            print(4)
            response['msg']='success'
            response['error_num']=0
    except Exception as e:
        print(str(e))
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)

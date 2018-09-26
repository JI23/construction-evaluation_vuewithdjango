from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from BTESDB.models import Project,Structure_response
from django.core import serializers
import requests
import json
from itertools import chain
import ast
def step6(request):
    response={}
    try:       
        #获取数据
        project=request.GET['project']
        data_list=request.GET.getlist('data[]',[])
        data1=request.GET.getlist('data1[]',[])
        data2=request.GET.getlist('data2[]',[])
        data3=request.GET.getlist('data3[]',[])
        data4=request.GET.getlist('data4[]',[])
        detail=[data1,data2,data3,data4]

        print(type(data_list),"::",data_list)
        print(type(data1),"::",data1)
        print(type(data2),"::",data2)
        print(type(data3),"::",data3)
        print(type(data4),"::",data4)
    except Exception as e:
        print (str(e))
        response['msg']='请完整填写结构响应信息！'
        response['error_num']=1
        return JsonResponse(response)
    #获取指向该项目的对象
    this_project=Project.objects.get(id=project)
    x=int(0)
    for item in data_list:
        #将string转化为dict
        a=ast.literal_eval(item)
        floor_no=int(a['floor_no'])
        earthquake_no=int(a['earthquake_no'])
        data=list()
        for i in range(floor_no):
            temp=list()
            line=ast.literal_eval(detail[x][i])
            print(line)
            for j in range(earthquake_no):
                key="earthquake"+str(j+1)
                temp.append(int(line[key]))
                print(line[key])
            data.append(temp)
        print(data)
        data=list(chain.from_iterable(data))
        if Structure_response.objects.filter(project=this_project,direction=a['direction'][0],
        EDP_type=a['EDP_type']).exists():
            #更新数据库中内容
            update=Structure_response.objects.get(project=this_project,direction=a['direction'][0],EDP_type=a['EDP_type'][0]) 
            update.floor_no=floor_no
            update.earthquake_no=earthquake_no
            update.data=data
            update.save()
            response['msg']='结构响应信息修改成功'
            response['error_num']=0
        else:
            #新增数据库中内容
            new=Structure_response(
                project=this_project,
                direction=a['direction'][0],
                EDP_type=a['EDP_type'][0],
                floor_no=a['floor_no'],
                earthquake_no=a['earthquake_no'],
                data=data)
            new.save()
            response['msg']='结构响应信息新增成功'
            response['error_num']=0
        x+=1
    return JsonResponse(response)

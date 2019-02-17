from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from BTESDB.models import *
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt

def edit(request):
    print ('edit')
    response={}
    try:
        username=request.GET['username']
        project=request.GET['project']
        this_user=User_Info.objects.get(username=username)

        print (project)
        base_info=Project.objects.filter(id=project,user=this_user)
        if base_info.exists():
            print(json.loads(serializers.serialize("json", base_info)))
            response['base_info']=json.loads(serializers.serialize("json", base_info))
        else:
            response['base_info']=''

        building_info=Building.objects.filter(project=project)
        if building_info.exists():
            print("building_info  exists")
            print(json.loads(serializers.serialize("json", building_info)))
            response['building_info']=json.loads(serializers.serialize("json", building_info))
        else:
            response['building_info']=''
        
        this_project=Project.objects.get(id=project)
        floor_info=Floor_Info.objects.filter(project=project)
        #.values_list('floor_no','floor_height','floor_area','influence_coefficient','population_density')
        if floor_info.exists():
            print('qqqqqqqqqqqqqqqqqqqqq')
            print(json.loads(serializers.serialize("json", floor_info)))
            response['floor_info']=(json.loads(serializers.serialize("json", floor_info)))
        else:
            print('mmmmmm')
            response['floor_info']=(json.loads(serializers.serialize("json", floor_info)))

        element_info=Element.objects.filter(project=project).values("start_floor","element_type","stop_floor","X","Y","Non","element__part_id","element__basic_unit")
        #Element.objects.filter(project=project)
        if element_info.exists():
            print('存在')
            print(element_info)
            response['element_info']=list(element_info)
            print(element_info)
        else:
            response['element_info']=''

        earthquake_info=Earthquake_Info.objects.filter(project=project)
        if earthquake_info.exists():
            print (json.loads(serializers.serialize("json", earthquake_info)))
            response['earthquake_info']=json.loads(serializers.serialize("json", earthquake_info))
        else:
            response['earthquake_info']=''
        
        wave_info=Earthquake_wave_detail.objects.filter(project=project)
        if wave_info.exists():
            print (json.loads(serializers.serialize("json", wave_info)))
            response['wave_info']=json.loads(serializers.serialize("json", wave_info))
        else:
            response['wave_info']=''

        structure_response=Structure_response.objects.filter(project=project).values("project","direction","EDP_type","floor_no","earthquake_no","data")
        if structure_response.exists():
            #处理data中的字符串，转变为[楼层数][地震数]的二维数组
            for item in structure_response:
                temp_list=item["data"][1:-1].split(", ")
                item["data"]=list()
                x=int(0)
                for i in range(item["floor_no"]):
                    t2=list()
                    for j in range(item["earthquake_no"]):
                        t2.append(Decimal(temp_list[x]))
                        x += 1
                    item["data"].append(t2)
                print (item["data"])
            print(structure_response)
            response['structure_response']=list(structure_response)
        else:
            response['structure_response']=''

        response['error_num']=0
        response['msg']='获取数据成功'
    except Exception as e:
        print (str(e))
        response['msg']='无法修改'
        response['error_num']=1
    return JsonResponse(response)

def delete(request):
    print(1)
    response={}
    #获取表单数据
    try:
        print (2)
        username=request.GET['username']
        print(username)
        project=request.GET['project']
        print (project)
        this_user=User_Info.objects.get(username=username)
        base_info=Project.objects.filter(user=this_user,id=project)
        if base_info.exists():
            base_info.delete()
        
        floor_info=Floor_Info.objects.filter(project=project)
        if floor_info.exists():
            floor_info.delete()

        element_info=Element.objects.filter(project=project)
        if element_info.exists():
            element_info.delete()

        earthquake_info=Earthquake_Info.objects.filter(project=project)
        if earthquake_info.exists():
            earthquake_info.delete()
        
        wave_info=Earthquake_wave_detail.objects.filter(project=project)
        if wave_info.exists():
            wave_info.delete()

        structure_response=Structure_response.objects.filter(project=project)
        if structure_response.exists():
            structure_response.delete()

        response['msg']='删除成功'
        response['error_num']=0       
    except Exception as e:
        print (str(e))
        response['msg']='删除失败'
        response['error_num']=1
    return JsonResponse(response)
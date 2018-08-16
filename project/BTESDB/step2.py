
from BTESDB.models import Project,User_Info,Floor_Info
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

def step2(request):
    print(1)
    #username=request.session['username']
    response={}
    
    project_name=request.GET['project_name']
    client_name=request.GET['client_name']
    project_leader=request.GET['project_leader']
    project_description=request.GET['project_description']
    print(project_name)
    try:
        print(2)
        #获取表单数据
        create_time=timezone.now().strftime("%Y-%m-%d")

        material=request.GET['material']
        structure_type=request.GET['structure_type']
        floor=request.GET['floors']
        figure_time=request.GET['figure_time']
        height=request.GET['height']
        area=request.GET['area']
        cost_per_squaremeter=request.GET['cost_per_squaremeter']
      
        #获取user外键
        this_user=User_Info.objects.get(username='13051997327')
        print(3.3)
        new=Project(user=this_user,
        project_name=project_name,
        client_name=client_name,
        project_description=project_description,
        create_time=create_time,
        project_leader=project_leader,
        material=material,
        structure_type=structure_type,
        floor=floor,
        figure_time=figure_time,
        height=height,
        area=area,
        cost_per_squaremeter=cost_per_squaremeter,
        is_finished=False,
        rate='0')
        
        new.save()
        print(3)
        response['project']=new.id
        print(4)
        #print (username)
        #print (project_name)
        response['msg']='success'
        response['error_num']=0
    except Exception as e:
        print (5)
        print (str(e))
        response['msg']=str(e)
        response['error_num']=1
    finally:
        return JsonResponse(response)

import ast

def saveFloor(request):
    print (1)
    #print(request.GET)
    project=request.GET['project']
    print(project)
    floor_list=request.GET.getlist('Floor_info[]',[])
    print(floor_list)
    response={}
    this_project=Project.objects.get(id=project)
    for item in floor_list:
        print (item)
        print (type(item))
        a=ast.literal_eval(item)
        #print(a["floor_no"])
        try:
            new=Floor_Info(
                project=this_project,
                floor_no=int(a['floor_no']),
                floor_height=float(a['floor_height']),
                floor_area=float(a['floor_area']),
                influence_coefficient=float(a['influence_coefficient']),
                population_density=float(a['population_density'])
            )
            new.save()
            response['msg']='success'
            response['error_num']=0
        except Exception as e:
            response['msg']=str(e)
            response['error_num']=1
    
    return JsonResponse(response)

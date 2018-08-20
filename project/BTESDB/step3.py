from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from BTESDB.models import DB_part,Element,Project,Damage_state_detail
from django.core import serializers
import requests
import json
def get_all_parts(request):
    response={}
    try:
        part_list = DB_part.objects.all()
        detail_list = Damage_state_detail.objects.all()
        response['msg']='success'
        response['error_num']=0
        response['list']  = json.loads(serializers.serialize("json", part_list))
        response['detail']  = json.loads(serializers.serialize("json", detail_list))
    except Exception as e:
        response['msg']=str(e)
        response['error_num']=1
        
    # print article_list
    # print type(article_list)
    #QuerySet是一个可遍历结构，包含一个或多个元素，每个元素都是一个Model实例
    #QuerySet类似于Python中的list，list的一些方法QuerySet也有，比如切片，遍历。
    #每个Model都有一个默认的manager实例，名为objects，QuerySet有两种来源：通过manager的方法得到、通过QuerySet的方法得到。mananger的方法和QuerySet的方法大部分同名，同意思，如filter(),update()等，但也有些不同，如manager有create()、get_or_create()，而QuerySet有delete()等
    #locals()返回一个包含当前作用域里面的所有变量和它们的值的字典。
    return JsonResponse(response)

import ast
def save_elements(request):
    print(1)
    #获得指向project的对象
    project=request.GET['project']
    this_project=Project.objects.get(id=project)
    print(2)
    #获取表单内容
    element_list=request.GET.getlist('tableData[]',[])
    print(3)
    print(element_list)
    response={}
    is_structure=request.GET['is_structure']
    if is_structure=='True':
        for item in element_list:
            print(4)
            print (item)
            print (type(item))
            a=ast.literal_eval(item)
            try:
                this_part=DB_part.objects.get(part_id=a['id'])
                start_floor=a['start_floor']
                stop_floor=a['stop_floor']
                new=Element(project=this_project,
                element_type='s',
                element=this_part,
                start_floor=start_floor,
                stop_floor=stop_floor)
                new.save()
                print(5)
                response['msg']='success'
                response['error_num']=0
            except Exception as e:
                print(str(e))
                response['msg']=str(e)
                response['error_num']=1
    else:
        for item in element_list:
            print(4)
            print (item)
            print (type(item))
            a=ast.literal_eval(item)
            try:
                this_part=DB_part.objects.get(part_id=a['id'])
                start_floor=a['start_floor']
                stop_floor=a['stop_floor']
                new=Element(project=this_project,
                element_type='n',
                element=this_part,
                start_floor=start_floor,
                stop_floor=stop_floor)
                new.save()
                print(5)
                response['msg']='success'
                response['error_num']=0
            except Exception as e:
                print(str(e))
                response['msg']=str(e)
                response['error_num']=1
    return JsonResponse(response)
        


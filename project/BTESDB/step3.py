from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from BTESDB.models import DB_part,Element,Project,Damage_state_detail
from django.core import serializers
import requests
import json
import time
from django.views.decorators.cache import cache_page
@cache_page(15)
def get_all_parts(request):
    response={}
    try:
        ctime=time.time()
        #part_list = DB_part.objects.all()
        temp=request.GET['value'][3]
        print(temp)
        part_list = DB_part.objects.filter(part_type=temp)
        detail_list= Damage_state_detail.objects.all()
        print(detail_list)

        second_first=DB_part.objects.filter(part_type=temp).values_list('first','second').distinct()
        second_first=list(second_first)
        print(second_first)
        response['second']=second_first

        first=DB_part.objects.filter(part_type=temp).values_list('first',flat=True).distinct()
        print (first)
        print(type(first))
        first=list(first)
        print(first)
        response['first']=first

        response['msg']='success'
        response['ctime']=ctime
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
    response={}
    #获取表单内容
    try:
        project=request.GET['project']
        floors=int(request.GET['floors'])   
        element_list=request.GET.getlist('tableData[]',[])
        is_structure=request.GET['is_structure']
    except Exception:
        response['msg']='请完整填写构件信息'
        response['error_num']=1
        return JsonResponse(response)

    #判断是结构构件还是非结构构件
    if is_structure=='True':
        element_type='s'
    else:
        element_type='n'
    #获得指向project的对象
    this_project=Project.objects.get(id=project)

    Element.objects.filter(project=this_project,element_type=element_type).delete()

    for item in element_list:
        #将string转化为dict
        a=ast.literal_eval(item)

        this_part=DB_part.objects.get(part_id=a['id'])
        start_floor=a['start_floor']
        stop_floor=a['stop_floor']

        if len(start_floor)==0:
            response['msg']='起始楼层不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:   
            try:
                start_floor=int(start_floor)
                if start_floor>=floors:
                    response['msg']='起始楼层最大为'+(floors-1)
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='起始楼层必须为整数'
                response['error_num']=1
                return JsonResponse(response)
            
        if len(stop_floor)==0:
            response['msg']='终止楼层不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:   
            try:
                stop_floor=int(stop_floor)
                if stop_floor>floors:
                    response['msg']='终止楼层最大为'+floors
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='终止楼层必须为整数'
                response['error_num']=1
                return JsonResponse(response)
        
        new=Element(project=this_project,
            element_type=element_type,
            element=this_part,
            start_floor=start_floor,
            stop_floor=stop_floor)
        new.save()

    response['msg']='构件信息存储成功'
    response['error_num']=0
            
    return JsonResponse(response)
        


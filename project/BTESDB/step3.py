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

    #删掉该project的所有element信息
    Element.objects.filter(project=this_project,element_type=element_type).delete()

    for item in element_list:
        #将string转化为dict
        a=ast.literal_eval(item)
        print(a)
        this_part=DB_part.objects.get(part_id=a['id'])
        start_floor=a['start_floor']
        print(start_floor)
        print(type(start_floor))
        stop_floor=a['stop_floor']
        X=a['X']
        Y=a['Y']
        Non=a['Non']

        if len(str(start_floor))==0:
            response['msg']='起始楼层不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:   
            try:
                start_floor=int(start_floor)
                if start_floor>floors:
                    response['msg']='起始楼层最大为'+str(floors)
                    response['error_num']=1
                    return JsonResponse(response)
                if start_floor<=0:
                    response['msg']='起始楼层最小为1'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception as e:
                print(str(e))
                response['msg']='起始楼层必须为整数'
                response['error_num']=1
                return JsonResponse(response)
            
        if len(str(stop_floor))==0:
            response['msg']='终止楼层不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:   
            try:
                stop_floor=int(stop_floor)
                if stop_floor>floors:
                    response['msg']='终止楼层最大为'+str(floors)
                    response['error_num']=1
                    return JsonResponse(response)
                if stop_floor<start_floor:
                    response['msg']='终止楼层不得小于起始楼层'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='终止楼层必须为整数'
                response['error_num']=1
                return JsonResponse(response)

        if len(str(X))==0:
            response['msg']='X方向易损件不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:
            try:
                X=float(X)
            except Exception:
                response['msg']='X方向易损件个数为实数！'
                response['error_num']=1
                return JsonResponse(response)

        if len(str(Y))==0:
            response['msg']='Y方向易损件不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:
            try:
                Y=float(Y)
            except Exception:
                response['msg']='Y方向易损件个数为实数！'
                response['error_num']=1
                return JsonResponse(response)
        
        if len(str(Non))==0:
            response['msg']='无方向易损件不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:
            try:
                Non=float(Non)
            except Exception:
                response['msg']='无方向易损件个数为实数！'
                response['error_num']=1
                return JsonResponse(response)

        if X==0 and Y==0 and Non==0:
            response['msg']='X、Y、无易损件个数不能同时为0！'
            response['error_num']=1
            return JsonResponse(response)
        
        new=Element(project=this_project,
            element_type=element_type,
            element=this_part,
            start_floor=start_floor,
            stop_floor=stop_floor,
            X=X,
            Y=Y,
            Non=Non)
        new.save()
        print('element')
        print(new.element)
        #到这也是字符型啊
    response['msg']='构件信息存储成功'
    response['error_num']=0
            
    return JsonResponse(response)
        


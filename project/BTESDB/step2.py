
from .models import Project,Building,Floor_Info
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from  decimal import Decimal
def step2(request):
    print('step 2')
    response={}
    try:
        #获取表单数据
        create_time=datetime.now()
        project=request.GET['project']
        material=request.GET['material']
        structure_type=request.GET['structure_type']
        floor=request.GET['floors']
        figure_time=request.GET['figure_time']
        height=request.GET['height']
        area=request.GET['area']
        cost_per_squaremeter=request.GET['cost_per_squaremeter']
        

        #检查数据合理性
        if len(material)==0:
            response['msg']='材料不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        elif len(material)>30:
            response['msg']='材料不能超过30个字符！'
            response['error_num']=1
            return JsonResponse(response)
        
        if len(structure_type)==0:
            response['msg']='结构类型不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        elif len(structure_type)>20:
            response['msg']='结构类型不能超过20个字符！'
            response['error_num']=1
            return JsonResponse(response)
        
        try:
            figure_time=datetime.strptime(figure_time,'%Y-%m-%d')
            if figure_time<=create_time:
                response['msg']='图审时间须在项目创建时间之后！'
                response['error_num']=1
                return JsonResponse(response)
        except Exception:
            response['msg']='图审时间格式：2018-8-18'
            response['error_num']=1
            return JsonResponse(response)
        print(floor)
        if len(floor)==0:
            response['msg']='楼层数量不能为空！' 
            response['error_num']=1
            return JsonResponse(response)   
        elif str(floor).isdigit()==False:
            response['msg']='楼层数量须为整数！'
            response['error_num']=1
            return JsonResponse(response)
        elif int(floor)<=0:
            response['msg']='楼层数量不能为零或负数！'
            response['error_num']=1
            return JsonResponse(response)
        print('here')
        if  len(height)==0:
            response['msg']='楼层总高不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        else:
            try:
                height=float(height)
                if height<=0:
                    response['msg']='楼层总高不能为零或负数！'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='楼层总高须为实数！'
                response['error_num']=1
                return JsonResponse(response)

        if len(area)==0:
            response['msg']='总面积不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:
            try:
                area=float(area)
                if area<=0:
                    response['msg']='总面积不能为零或负数！'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='总面积须为实数！'
                response['error_num']=1
                return JsonResponse(response)
        
        if len(cost_per_squaremeter)==0:
            print('造价为空')
        else:
            try:
                cost_per_squaremeter=float(cost_per_squaremeter)
                if cost_per_squaremeter<=0:
                    response['msg']='每平米造价不能为零或负数！'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='每平米造价必须为实数'
                response['error_num']=1
                return JsonResponse(response)

        if Building.objects.filter(project_id=project).exists():
            print('更新')
            update=Building.objects.get(project=project)
            update.material=material
            update.structure_type=structure_type
            update.floor=floor
            update.figure_time=figure_time
            update.height=height
            update.area=area
            update.cost_per_squaremeter=cost_per_squaremeter
            update.save()
            response['msg']='建筑信息修改成功'
            response['error_num']=0
        else:
            print('新建')
            this_project=Project.objects.get(id=project)
            new=Building(project=this_project,
            material=material,
            structure_type=structure_type,
            floor=floor,
            figure_time=figure_time,
            height=height,
            area=area,
            cost_per_squaremeter=cost_per_squaremeter)            
            new.save()
            response['msg']='建筑信息新建成功'
            response['error_num']=0
        saveFloor(request)
    except Exception as e:
        print (str(e))
        response['msg']=str(e)
        response['error_num']=1   
    return JsonResponse(response)

import ast
from django.db.models import Max,Min,Sum
def saveFloor(request):
    response={}
    #print(request.GET)
    try:
    #获取表单数据
        project=request.GET['project']
        floors=int(request.GET['floors'])
        area=float(request.GET['area'])
        height=float(request.GET['height'])
        floor_list=request.GET.getlist('Floor_info[]',[])        
        #print(floor_list)
    except Exception as e :
        print (str(e))
        response['msg']='请先正确填写楼层信息'
        response['error_num']=1
        return JsonResponse(response)

    this_project=Project.objects.get(id=project)
    
    for item in floor_list:
        #将string转化为dictlen(str(a['floor_no']))==0:
        a=ast.literal_eval(item)
        if len(str(a['floor_no']))==0:
         #if len(a['floor_no'])==0:
            response['msg']='楼层编号不能为空！' 
            response['error_num']=1
            return JsonResponse(response)
        else:   
            try:
                floor_no=int(a['floor_no'])
                if floor_no>floors or floor_no==0:
                    response['msg']='楼层编号不得大于楼层总数或等于0！'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='楼层编号必须为整数'
                response['error_num']=1
                return JsonResponse(response)

        if len(a['floor_height'])==0:
            response['msg']='楼层高度不能为空！' 
            response['error_num']=1
            return JsonResponse(response)   
        else:
            try:
                floor_height=float(a['floor_height'])
                if floor_height<=0 or floor_height>height:
                    response['msg']='楼层高度零或负数或超过总高度！'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='楼层高度须为实数！'
                response['error_num']=1
                return JsonResponse(response)

        if len(a['floor_area'])==0:
            response['msg']='楼层面积不能为空！' 
            response['error_num']=1
            return JsonResponse(response)   
        else:
            try:
                floor_area=float(a['floor_area'])
                if floor_area<=0 or floor_area>area:
                    response['msg']='楼层面积不能小于0或超过总面积！'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='楼层面积须为实数！'
                response['error_num']=1
                return JsonResponse(response)
        print (a['influence_coefficient'])
        if len(a['influence_coefficient'])==0:
            response['msg']='楼层影响系数不能为空！' 
            response['error_num']=1
            return JsonResponse(response)   
        else:
            try:
                influence_coefficient=float(a['influence_coefficient'])
                if influence_coefficient<1 or influence_coefficient>1.5:
                    response['msg']='楼层影响系数在1到1.5之间'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='楼层影响系数须为实数！'
                response['error_num']=1
                return JsonResponse(response)

        if len(a['population_density'])==0:
            response['msg']='楼层人口密度不能为空！' 
            response['error_num']=1
            return JsonResponse(response)   
        else:
            try:
                population_density=float(a['population_density'])
                if population_density<0 :
                    response['msg']='人口密度不能小于0'
                    response['error_num']=1
                    return JsonResponse(response)
            except Exception:
                response['msg']='楼层人口密度必须为实数！'
                response['error_num']=1
                return JsonResponse(response)

        
        if Floor_Info.objects.filter(project=this_project,floor_no=int(a['floor_no'])).exists():
            #定位到此楼层对应的数据库条目
            print('开始修改')
            update=Floor_Info.objects.get(project=this_project,floor_no=int(a['floor_no']))
            update.floor_height=float(a['floor_height'])
            update.floor_area=float(a['floor_area'])
            update.influence_coefficient=float(a['influence_coefficient'])
            update.population_density=float(a['population_density'])
            update.save()
            response['msg']='修改成功'
            response['error_num']=0
        else:
            print(a)
            print(float(a['influence_coefficient']))
            print(Decimal(a['influence_coefficient']))
            new=Floor_Info(
                project=this_project,
                floor_no=int(a['floor_no']),
                floor_height=float(a['floor_height']),
                floor_area=float(a['floor_area']),
                influence_coefficient=float(a['influence_coefficient']),
                population_density=float(a['population_density']))
            new.save()
            response['msg']='新建成功'
            response['error_num']=0
    if Floor_Info.objects.filter(project=this_project).count()!=floors:
        response['msg']='请填写完所有楼层信息！'
        response['error_num']=1
        return JsonResponse(response)
    if Floor_Info.objects.filter(project=this_project).aggregate(Sum('floor_area'))['floor_area__sum']!=area:
        print(area)
        print (Floor_Info.objects.filter(project=this_project).aggregate(Sum('floor_area'))['floor_area__sum'])
        response['msg']='楼层面积和不等于总面积！'
        response['error_num']=1
        return JsonResponse(response)
    if Floor_Info.objects.filter(project=this_project).aggregate(Sum('floor_height'))['floor_height__sum']!=height:
        response['msg']='楼层高度和不等于总高度！'
        response['error_num']=1
        return JsonResponse(response)
    #return JsonResponse(response)

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from .models import Earthquake_Info,Project,Earthquake_wave_detail
from django.core import serializers
import requests
import json

def step5(request):
    response={}
    try:
        #获取数据
        project=request.GET['project']
        defense_intensity=request.GET['defense_intensity']
        site_type=request.GET['site_type']
        number=request.GET['number']       
        group=request.GET['group']
        earthquake_level=request.GET['earthquake_level']
        peak_acceleration=request.GET['peak_acceleration']
    except Exception:
        response['msg']='请正确填写数据'
        response['error_num']=1
        return JsonResponse(response)

    #检验地震波数合理性
    if len(number)==0:
        response['msg']='地震波数不能为空！' 
        response['error_num']=1
        return JsonResponse(response)
    else:   
        try:
            number=int(number)
            if number<=0:
                response['msg']='地震波数大于0！'
                response['error_num']=1
                return JsonResponse(response)
        except Exception:
            response['msg']='地震波数必须为整数'
            response['error_num']=1
            return JsonResponse(response)

    #获取指向该项目的对象   
    this_project=Project.objects.get(id=project)
    if Earthquake_Info.objects.filter(project=this_project).exists():
        print('更新')
        #更新数据库中内容
        update=Earthquake_Info.objects.get(project=this_project)
        update.defense_intensity=defense_intensity
        update.site_type=site_type
        update.number=number
        update.group=group
        update.earthquake_level=earthquake_level
        update.peak_acceleration=peak_acceleration
        update.save()
        response['msg']='修改成功'
        response['error_num']=0
    else:
        #在数据库中新建
        print('新建')
        new=Earthquake_Info(
            project=this_project,
            defense_intensity=defense_intensity,
            site_type=site_type,
            number=number,
            group=group,
            peak_acceleration=peak_acceleration,
            earthquake_level=earthquake_level)
        new.save()
        response['msg']='新建成功'
        response['error_num']=0   
    save_waves(request)
    return JsonResponse(response)

import ast
import json
import os
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def save_wave_file(request):
    print('save_wave_file')
    response={}
    try:
        print(request.FILES)
        f=request.FILES.get('test')
        username=request.POST['username']
        project=request.POST['project']
        #wave_no=request.POST['wave_no']
        #print(wave_no)
        print(username)
        print(project)
        #print(wave_no)
        print(f.name)
        d='media/project/'+project+'/wave_files/'
        folder=os.path.exists(d)
        if not folder:
            os.makedirs(d)
            print('创建文件夹成功')
        else:
            for files in os.listdir(d):
                filesname=files.split('/')[-1]
                if filesname==f.name:
                    os.remove('media/project/'+project+'/wave_files/'+f.name)
                    print('删除同名文件成功')          
        with open(d+'/'+f.name,'wb+') as dest:
            for chunk in f.chunks():      # 分块写入文件
                dest.write(chunk)
        response['error_num']=0
        response['msg']='文件获取并保存成功'
    except Exception as e:
        print (str(e))
    return JsonResponse(response)
def save_waves(request):
    response={}
    try:  
        #获取表单内容
        print(request)
        project=request.GET['project']
        wave_list=request.GET.getlist('earthquake_info[]',[])
        print(wave_list)
        number=request.GET['number']
    except Exception as e:
        print (str(e))
        response['msg']='请正确填写数据'
        response['error_num']=1
        return JsonResponse(response)
    #获得指向project的对象   
    this_project=Project.objects.get(id=project)
    row=int(0)
    for item in wave_list:
        print("将string转化为dict")
        a=ast.literal_eval(item)
        #检验数据合理性
        if len(str(a['earthquake_no']))==0:
            response['msg']='地震波编号不能为空！' 
            response['error_num']=1
            return JsonResponse(response) 
        else:
            try:
                earthquake_no=int(a['earthquake_no'])
                if earthquake_no<=0 or earthquake_no>int(number):
                    #print(number+1)
                    response['msg']='地震波编号不能小于0或大于地震波数！' 
                    response['error_num']=1
                    return JsonResponse(response) 
            except Exception as e:
                print(str(e))
                response['msg']='地震波编号必须为整数！' 
                response['error_num']=1
                return JsonResponse(response)

        if len(a['peak'])==0:
            response['msg']='地震波峰值不能为空！' 
            response['error_num']=1
            return JsonResponse(response) 
        else:
            try:
                peak=float(a['peak'])
                if peak<=0 :
                    response['msg']='地震波峰值不能小于0！' 
                    response['error_num']=1
                    return JsonResponse(response) 
            except Exception:
                response['msg']='地震波峰值必须为实数！' 
                response['error_num']=1
                return JsonResponse(response) 
        
        if Earthquake_wave_detail.objects.filter(project=this_project,earthquake_wave_no=earthquake_no).exists():
            #更新数据库内容
            update=Earthquake_wave_detail.objects.get(project=this_project,earthquake_wave_no=earthquake_no)
            update.earthquake_wave_name=a['name']
            update.peak=peak
            d='media/project/'+project+'/wave_files/'
            folder=os.path.exists(d)
            if not folder:
                path='null'
            else:
                files=os.listdir(d)
                path='project/'+project+'/wave_files/'+files[row]
                #row += 1
            update.earthquake_wave_file=path
            update.save()
            response['msg']='地震波修改成功'
            response['error_num']=0 
        else:
            #对数据库内容进行新增
            #地震波文件仅保存其目录
            d='media/project/'+project+'/wave_files/'
            folder=os.path.exists(d)
            if not folder:
                path='null'
            else:
                files=os.listdir(d)
                path='project/'+project+'/wave_files/'+files[row]
                #row += 1
            new=Earthquake_wave_detail(project=this_project,
                earthquake_wave_no=earthquake_no,
                earthquake_wave_name=a['name'],
                peak=peak,
                earthquake_wave_file=path)
            new.save()
            response['msg']='地震波信息新建成功'
            response['error_num']=0
    if Earthquake_wave_detail.objects.filter(project=this_project).count()!=int(number):
        print("请填写完所有地震信息！")
        response['msg']='请填写完所有地震信息！'
        response['error_num']=1        
    return JsonResponse(response)



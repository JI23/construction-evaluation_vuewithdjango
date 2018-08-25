

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Project,User_Info,DB_part,DB_template
from django.contrib import auth
from django import forms    #导入表单
from django.contrib.auth.models import User   #导入django自带的user表
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    #主页
    try:
        username=request.session['username']
        this_user=User_Info.objects.get(username=username)
        project_list=Project.objects.filter(user=this_user)
    except Exception:
        print('还没登陆')
    finally:
        return render(request,'index.html',locals())

def logout(request):
    #登出
    auth.logout(request)
    return render(request,'index.html')
@csrf_exempt
def show_projects(request):
    response = {}
    try:
        print (1)
        #print (request)
        is_finished=request.GET['is_finished']
        username=request.GET['username']
        print (is_finished)
        this_user=User_Info.objects.get(username=username)
        if is_finished=='False':
            projects = Project.objects.filter(is_finished=0,user=this_user)
        else:
            projects = Project.objects.filter(is_finished=1,user=this_user)
        response['list']  = json.loads(serializers.serialize("json", projects))
        response['msg'] = 'success'
        response['error_num'] = 0
        #print (response)
    except  Exception as e:
        print (2)
        response['msg'] = str(e)
        response['error_num'] = 1
    print (3)
    return JsonResponse(response)

def uploadImg(request):  
    if request.method=='POST':
        xmls=request.FILES.getlist('xml',[])
        for item in xmls:
            xml=item
            name=item.name
            name='.'.join(name.split('.')[0:4])
            print (name)
            try:
                this_part=DB_part.objects.get(part_id=name)
                this_part.delete()
            except Exception:
                print (str(Exception))

            get=DB_template.objects.get(part_id=name)
            this_user=User_Info.objects.get(username='13051997327')
            
            print (get)
            if get.TypeName=='Acceleration':
                EDP_type='A'
            else:
                EDP_type='S'
            if get.Official=='True':
                is_formal=1
            else:
                is_formal=0
            new=DB_part(user=this_user,
            part_id=get.part_id,
            part_name=get.Name,
            EDP_type=EDP_type,
            data_resource=get.Author,
            is_formal=is_formal,
            part_type='c',
            description=get.Description,
            xml=xml
            )
            new.save()

        return HttpResponse('成功')
        
    return render(request,'upload.html')
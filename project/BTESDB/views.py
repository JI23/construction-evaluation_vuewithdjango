

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

def Rating(a):
    b=0
    if a=='N/A':
        b='1'
    elif a=='Marginal':
        b='2'
    elif a=='Average':
        b='3'
    elif a=='Superior':
        b='4'
    return b
def Judge(a):
    b=0
    if a=='true' or a=='1' or a==1:
        b=1
    return b
import xml.etree.ElementTree as ET
import os

def upload(request):
    if request.method=='POST':
        xmls=request.FILES.getlist('xml',[])
        t=request.POST['type']
        for item in xmls:
            xml=item
            name=item.name
            name=name.split('.')
            name.pop()
            name='.'.join(name)
            #name='.'.join(name.split('.')[0:4])
            print (name)
            
            d={}#每个part_id对应一条字典信息
            x=[]
            
            tree=ET.ElementTree(file=xml)
            root=tree.getroot()
            d[root.tag]=root.attrib

            for child_of_root in root:
                d[child_of_root.tag]=child_of_root.text
                for child2 in child_of_root:
                    d[child2.tag]=child2.text
                    if child2.tag=='DamageState':
                        x.append(child2)
            damage_state_number=len(x)
            print (d)
            print(damage_state_number)

            if d['TypeName']=='Acceleration':
                EDP_type='A'
            else:
                EDP_type='S'
            if d['Notes']==None:
                d['Notes']='None'
            if ('Cost' in d.keys()) ==False:
                d['Cost']=0.0
            elif d['Cost']==None:
                d['Cost']=0.0
            if d['Author']==None:
                d['Author']='None'

            this_user=User_Info.objects.get(id=1)

            new=DB_part(user=this_user,
            part_id=d['ID'],
            description=d['Description'],
            basic_unit=d['BasicUnit'],
            cost=d['Cost'],
            part_name=d['Name'],
            data_resource=d['Author'],
            correlation=Judge(d['Correlation']),
            directional=Judge(d['Directional']),
            EDP_type=EDP_type,
            default_units=d['DefaultUnits'],
            user_defined=Judge(d['UserDefined']),
            DataQuality=Rating(d['DataQuality']),
            DataRelevance=Rating(d['DataRelevance']),
            Documentation=Rating(d['Documentation']),
            Rationality=Rating(d['Rationality']),
            is_formal=Judge(d['Official']),
            create_date=d['DateCreated'],
            Approved=Judge(d['Approved']),
            Incomplete=Judge(d['Incomplete']),
            #Notes=d['Notes'],
            UseEDPValueOfFloorAbove=Judge(d['UseEDPValueOfFloorAbove']),
            DSGroupType=d['DSGroupType'],
            damage_state_number=damage_state_number,
            part_type=t[0],                     
            xml=xml)
            try:
                this_part=DB_part.objects.get(part_id=name)
                path="media/"+t+"/"
                dest="media/"+t+"/"+name+'/'+item.name
                print(dest)
                if os.path.exists(dest):
                    for each in os.listdir(path):
                        if each.name.endwith('.xml'):
                            os.remove(dest)
                    print('删除成功')
                this_part.description=d['Description']
                this_part.basic_unit=d['BasicUnit']
                this_part.cost=d['Cost']
                this_part.part_name=d['Name']
                this_part.data_resource=d['Author']
                this_part.correlation=Judge(d['Correlation'])
                this_part.directional=Judge(d['Directional'])
                this_part.EDP_type=EDP_type
                this_part.default_units=d['DefaultUnits']
                this_part.user_defined=Judge(d['UserDefined'])
                this_part.DataQuality=Rating(d['DataQuality'])
                this_part.DataRelevance=Rating(d['DataRelevance'])
                this_part.Documentation=Rating(d['Documentation'])
                this_part.Rationality=Rating(d['Rationality'])
                this_part.is_formal=Judge(d['Official'])
                this_part.create_date=d['DateCreated']
                this_part.Approved=Judge(d['Approved'])
                this_part.Incomplete=Judge(d['Incomplete'])
                #this_part.Notes=d['Notes']
                this_part.UseEDPValueOfFloorAbove=Judge(d['UseEDPValueOfFloorAbove'])
                this_part.DSGroupType=d['DSGroupType']
                this_part.damage_state_number=damage_state_number
                this_part.part_type=t[0]                   
                this_part.xml=xml
                this_part.save()
                print('更新成功')
                continue
            except Exception as e:
                print (str(e))
            new.save()
    return render(request,'upload.html')

def upload_db_part(request):  
    if request.method=='POST':
        xmls=request.FILES.getlist('xml',[])
        for item in xmls:
            xml=item
            name=item.name
            name=name.split('.')
            name.pop()
            name='.'.join(name)
            #name='.'.join(name.split('.')[0:4])
            print (name)

            d={}#每个part_id对应一条字典信息
            tree=ET.ElementTree(file=xml)
            root=tree.getroot()
            d[root.tag]=root.attrib

            for child_of_root in root:
                d[child_of_root.tag]=child_of_root.text
                for child2 in child_of_root:
                    d[child2.tag]=child2.text
            print (d)
            try:
                this_part=DB_part.objects.get(part_id=name)
                #this_part.delete()
                continue
            except Exception as e:
                print (str(e))

            get=DB_template.objects.get(part_id=name)
            this_user=User_Info.objects.get(username='123456')
            
            print (get)
            if get.TypeName=='Acceleration':
                EDP_type='A'
            else:
                EDP_type='S'
            if get.Official=='TRUE':
                is_formal=1
            else:
                is_formal=0
            if get.user_defined=='FALSE':
                get.user_defined=0
            else:
                get.user_defined=1
            
            get.part_type=get.part_type[0]
            
            new=DB_part(user=this_user,
            part_id=get.part_id,
            part_name=get.Name,
            EDP_type=EDP_type,
            data_resource=get.Author,
            is_formal=is_formal,
            part_type=get.part_type,
            description=get.Description,
            user_defined=get.user_defined,
            xml=xml
            )
            new.save()

        return HttpResponse('成功')
        
    return render(request,'upload.html')

    
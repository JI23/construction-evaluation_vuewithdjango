

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
def brief_projects(request):
    response = {}
    try:
        un_projects = Project.objects.filter(is_finished=0).count()
        ed_projects = Project.objects.filter(is_finished=1).count() 
        sum_projects = un_projects+ed_projects
        response['all']  = sum_projects
        response['success'] = ed_projects
        response['unsuccess'] = un_projects
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    
def logout(request):
    #登出
    auth.logout(request)
    return render(request,'index.html')
@csrf_exempt
def show_projects(request):
    print('show_projects')
    response = {}
    try:
        is_finished=request.GET['is_finished']
        username=request.GET['username']
        print (is_finished)
        this_user=User_Info.objects.get(username=username)
        print(this_user)
        if is_finished=='False':
            projects = Project.objects.filter(is_finished=0,user=this_user) 
        else:
            projects = Project.objects.filter(is_finished=1,user=this_user)       
        response['list']  = json.loads(serializers.serialize("json", projects))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        print(str(e))
        response['msg'] = str(e)
        response['error_num'] = 1
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
def classify_first(name):
    if name=='BE':
        return 'BE — 外部建筑构架'
    elif name=='BI':
        return 'BI — 内部建筑构件'
    elif name=='MEP':
        return 'MEP — 机电构件'
    elif name=='S':
        return 'S — 特殊设备及家具'
    else:
        return name+' — 分类不明'
def classify_second(first,second):
    if first=='BE':
        if second=='F':
            return '幕墙'
        elif second=='W':
            return '门窗'
        elif second=='D':
            return '外墙装饰'
        else:
            return '分类不明'
    elif first=='BI':
        if second=='C':
            return '吊顶'
        elif second=='D':
            return '内装'
        elif second=='S':
            return '楼梯'
        elif second=='P':
            return '隔墙'
        else:
            return '分类不明'
    elif first=='MEP':
        if second=='P':
            return '水专业构件'
        elif second=='M':
            return '暖通专业构件'
        elif second=='E':
            return '电专业构件'
        elif second=='L':
            return '电梯'
        else:
            return '分类不明'
    elif first=='S':
        if second=='E':
            return '设备'
        elif second=='F':
            return '家具'
        else:
            return '分类不明'
    else:
        return '分类不明'
def classify_FEMA1(name):
    d={'A':'Substructure','B':'Shell','C':'Interiors','D':'Services',
    'E':'Equipment & Furnishings','F':'Special Construction & Demolition'}
    return d[name]
def classify_FEMA2(name):
    A={'A1O11': 'Wall Foundations','A1012': 'Column Foundations & Pile Caps',
    'A1013': 'Perimeter Drainage & Insulation',
    'B1031':'Steel Columns','B1033':'Steel Braces','B1035':'Steel Connections',
    'B1041':'Reinforced Concrete or Composite Columns','B1044':'Reinforced Concrete or Composite Shearwalls',
    'B1049':' ','B1051':' ','B1052':' ','B1061':' ','B1071':' ',
    'B2011':'Exterior Wall Construction','B2022':'Curtain Walls','B2023':'Storefronts',
    'B3011':'Roof Finishes','B3031':' ','B3041':' ',
    'C1011':'Fixed Partitions','C2011':'Regular Stairs','C3011':'',
    'C3021':' ','C3027':'Access Pedastal Flooring','C3032':'Suspended Ceilings',
    'C3033':'Recessed Ceiling Lighting','C3034':'Independent Pendant Lighting',
    'D1014':' ','D2021':'Cold Water Service','D2022':'Hot Water Service',
    'D2031':'Waste Piping','D2051':' ','D2061':' ','D3031':'Chilled Water Systems',
    'D3032':'Direct Expension Systems','D3041':'Air Distribution Systems','D3052':'Package Units',
    'D3067':'Energy Monitoring & Control','D4011':'Sprinkler Water Supply','D5011':'High Tension Service & Dist',
    'D5012':'Low Tension Service & Dist','D5092':'Emergency Light & Power Systems',
    'E2022':'Furniture & Accessories',
    'F1012':'Pre-engineered Structures'}
    try:
        return A[name]
    except Exception as e:
        print (str(e))
        return '分类不明'
from datetime import datetime,timedelta
def get_datetime(dt):
    year=int(dt[0:4])
    month=int(dt[5:7])
    day=int(dt[8:10])
    hour=int(dt[11:13])
    minute=int(dt[14:16])
    second=int(dt[17:19])
    mic=int(dt[20:26])
    #delta=int(dt[-4])
    dt=datetime(year,month,day,hour,minute,second,mic)
    #dt=dt+timedelta(hours=delta)
    print (dt)
    return dt


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
            #获取结构构件的分类信息
            first=second=' '
            if t=='common':
                first=classify_first(name[0])
                second=classify_second(name[0],name[1])
            elif t=='fema':
                first=classify_FEMA1(name[0][0])
                second=classify_FEMA2(name[0])
            print(first)
            print(len(first))
            print(second)
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

            try:
                this_part=DB_part.objects.get(part_id=name)
                path="media/"+t+"/"
                dest="media/"+t+"/"+name+'/'+item.name
                print(dest)
                if os.path.exists(dest):
                    for each in os.listdir(path+name):
                        if each.endswith('.xml'):
                            print(each)
                            os.remove(path+name+'/'+each)
                            print('删除成功')
                this_part.description=d['Description']
                this_part.first=first
                this_part.second=second
                this_part.basic_unit=d['BasicUnit']
                this_part.cost=d['Cost']
                this_part.part_name=d['Name']
                this_part.data_resource=d['Author']
                this_part.EDP_type=EDP_type
                this_part.user_defined=Judge(d['UserDefined'])
                this_part.create_date=get_datetime(d['DateCreated'])
                this_part.damage_state_number=damage_state_number
                this_part.part_type=t[0]                   
                this_part.xml=xml
                this_part.save()
                print('更新成功')
                continue
                '''
                this_part.correlation=Judge(d['Correlation'])
                this_part.directional=Judge(d['Directional'])
                this_part.default_units=d['DefaultUnits']
                this_part.DataQuality=Rating(d['DataQuality'])
                this_part.DataRelevance=Rating(d['DataRelevance'])
                this_part.Documentation=Rating(d['Documentation'])
                this_part.Rationality=Rating(d['Rationality'])
                this_part.is_formal=Judge(d['Official'])
                this_part.Approved=Judge(d['Approved'])
                this_part.Incomplete=Judge(d['Incomplete'])                                
                #this_part.Notes=d['Notes']
                this_part.UseEDPValueOfFloorAbove=Judge(d['UseEDPValueOfFloorAbove'])
                this_part.DSGroupType=d['DSGroupType']
                '''
            except Exception as e:
                print (str(e))
                new=DB_part(user=this_user,
                part_id=d['ID'],
                first=first,
                second=second,
                description=d['Description'],
                basic_unit=d['BasicUnit'],
                cost=d['Cost'],
                part_name=d['Name'],
                data_resource=d['Author'],
                is_formal=Judge(d['Official']),
                user_defined=Judge(d['UserDefined']),
                EDP_type=EDP_type,
                damage_state_number=damage_state_number,
                create_date=get_datetime(d['DateCreated']),
                part_type=t[0],                     
                xml=xml)
                new.save()
            '''
            correlation=Judge(d['Correlation']),
            directional=Judge(d['Directional']),
            default_units=d['DefaultUnits'],           
            DataQuality=Rating(d['DataQuality']),
            DataRelevance=Rating(d['DataRelevance']),
            Documentation=Rating(d['Documentation']),
            Rationality=Rating(d['Rationality']),         
            Approved=Judge(d['Approved']),
            Incomplete=Judge(d['Incomplete']),
            #Notes=d['Notes'],
            UseEDPValueOfFloorAbove=Judge(d['UseEDPValueOfFloorAbove']),
            DSGroupType=d['DSGroupType'],
            '''
            
    return render(request,'upload.html')



    
import ast
from django.db.models import Max,Min,Sum

from .models import DB_part,User_Info
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def savegen(request):
    response={}

    gen_info=request.GET['gen_info']
    print(type(gen_info))
    print(gen_info)   
    #将string转化为dict
    gen_info=ast.literal_eval(gen_info)
    print(type(gen_info))

    notes_info=request.GET['notes_info']
    print(type(notes_info))
    print(notes_info)
    #将string转化为dict
    notes_info=ast.literal_eval(notes_info)
    print(type(notes_info))

    username=request.GET['username']
    #调用此函数，生成xml文件，保存在media/user_defined文件夹下
    addDBpart(gen_info,notes_info,username)

    
    this_user=User_Info.objects.get(username=username)
    path='user_defined/'+username+'/'+gen_info['id']+'/'+gen_info['id']+'.xml'
    new=DB_part(user=this_user,
    part_id=gen_info['id'],
    part_name=gen_info['name'],
    EDP_type='A',
    data_resource=notes_info['author'],
    is_formal=0,
    part_type='u',
    description=gen_info['description'],
    user_defined=1,
    xml=path)
    new.save()

    response['msg']='保存成功'
    response['error_num']=0
    return JsonResponse(response)

import xml.etree.ElementTree as ET
import os
def addDBpart(gen_info,notes_info,username):
    print (gen_info['name'])
    root=ET.Element('FragilityCurve',{'FileVersion':'"2.0"'})
    
    UniqueID=ET.SubElement(root,'UniqueID');UniqueID.text=' '
    ID=ET.SubElement(root,'ID');ID.text=gen_info['id']
    Description=ET.SubElement(root,'Description');Description.text=gen_info['description']
    BasicUnit=ET.SubElement(root,'BasicUnit');BasicUnit.text=' '
    Cost=ET.SubElement(root,'Cost');Cost.text='0'
    Name=ET.SubElement(root,'Name');Name.text=gen_info['name']
    Author=ET.SubElement(root,'Author');Author.text=notes_info['author']
    Correlation=ET.SubElement(root,'Correlation');Correlation.text=gen_info['choose2']
    Directional=ET.SubElement(root,'Directional');Directional.text=gen_info['choose1']
    
    #EDPType
    EDPType=ET.SubElement(root,'EDPType')
    Dimension=ET.SubElement(EDPType,'Dimension');Dimension.text=gen_info['DP_Dimension']
    TypeName=ET.SubElement(EDPType,'TypeName');TypeName.text=gen_info['typename']
    DefaultUnits=ET.SubElement(EDPType,'DefaultUnits');DefaultUnits.text=str(gen_info['units'])
    UserDefined=ET.SubElement(EDPType,'UserDefined');UserDefined.text='false'
    
    #Ratings
    Ratings=ET.SubElement(root,'Ratings');Ratings.text=' '
    DataQuality=ET.SubElement(Ratings,'DataQuality');DataQuality.text=notes_info['quality']
    DataRelevance=ET.SubElement(Ratings,'DataRelevance');DataRelevance.text=notes_info['relevance']
    Documentation=ET.SubElement(Ratings,'Documentation');Documentation.text=notes_info['data']
    Rationality=ET.SubElement(Ratings,'Rationality');Rationality.text=notes_info['rationality']

    Official=ET.SubElement(root,'Official');Official.text='false'
    DateCreated=ET.SubElement(root,'DateCreated');DateCreated.text='2018-04-17 22:19:44.744'
    Approved=ET.SubElement(root,'Approved');Approved.text=gen_info['value2']
    Incomplete=ET.SubElement(root,'Incomplete');Incomplete.text='false'
    Notes=ET.SubElement(root,'Notes');Notes.text=notes_info['notes']
    UseEDPValueOfFloorAbove=ET.SubElement(root,'UseEDPValueOfFloorAbove');UseEDPValueOfFloorAbove.text=gen_info['value1']

    DamageStates=ET.SubElement(root,'DamageStates')
    DSGroupType=ET.SubElement(DamageStates,'DSGroupType'); DSGroupType.text='Sequential'
    
    tree=ET.ElementTree(root)
    print(type(tree))
    
    path='media/user_defined/'+username+'/'+gen_info['id']+'/'+gen_info['id']+'.xml'
    d='media/user_defined/'+username+'/'+gen_info['id']+'/'
    folder = os.path.exists(d)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
	    os.makedirs(d)            #makedirs 创建文件时如果路径不存在会创建这个路径
	    print ('创建文件夹成功')
    tree.write(path)
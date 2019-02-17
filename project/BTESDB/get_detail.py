from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Project,User_Info,DB_part
from django.contrib import auth
from django import forms    #导入表单
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
import os
import os.path
import re
import codecs
import xml.etree.ElementTree as ET

def get_detail(request):
    print("get_detail")
    response={}
    #获取数据
    try:
        part_id=request.GET['part_id']
        #id=request.GET['id']
        this_part=DB_part.objects.get(part_id=part_id)
        print("成功获取")
        path=this_part.xml.url
        print(path)
        #调用函数，解析xml文件
        d=xmlAnalysis(path)
        response['aaa']=d
        DamageStates=d['DamageStates']
        for item in d:
            print(item)
        
        for item in DamageStates:
            print(item)
        #存了除了损伤状态外的所以参数
        response['detail']=d
        #每个object代表一个损伤状态
        response['DamageStates']=DamageStates
        response['error_num']=0
        response['msg']='获取详情成功'
    except Exception as e:
        print(str(e))
        response["error_num"]=1
        response['msg']='获取详情失败'
    return JsonResponse(response)

def xmlAnalysis(path):
    try:
        d={}#每个part_id对应一条字典信息
        l=[]#存储解析后的DamageState中的信息
        CostConsequence={}
        TimeConsequence={}
        x=[]#存储DamageState的对象,len(x)就是DamageState的个数
        y=[]
        path="."+path
        tree=ET.ElementTree(file=path)
        root=tree.getroot()
        d[root.tag]=root.attrib
        for child_of_root in root:
            d[child_of_root.tag]=child_of_root.text
            #d1[child_of_root.tag]=child_of_root.text
            for child2 in child_of_root:
                d[child2.tag]=child2.text
                #d1[child2.tag]=child2.text
                if child2.tag=='DamageState':
                    x.append(child2)
        #print(len(x))
        for k in range(0,len(x)):
            l.append({})
            y.append({})
        #print(y)
        for i in range(0,len(x)):
            for child3 in x[i]:
                l[i][child3.tag]=child3.text
                for child4 in child3:
                    l[i][child4.tag]=child4.text
                    if child4.tag=='CostConsequence':
                        for child5 in child4:
                            CostConsequence[child5.tag]=child5.text
                    elif child4.tag=='TimeConsequence':
                        for child5 in child4:
                            TimeConsequence[child5.tag]=child5.text
                    l[i]['CostConsequence']=CostConsequence
                    l[i]['TimeConsequence']=TimeConsequence
        d['DamageStates']=l 
        
        d1={}
        re_cost={}
        re_time={}
        d1['id']=d['ID']
        d1['description']=d['Description']
        d1['name']=d['Name']
        d1['choose2']=d['Correlation']
        d1['choose1']=d['Directional']
        d1['value2']=d['Approved']
        d1['value1']=d['UseEDPValueOfFloorAbove']
        d1['DP_Dimension']=d['Dimension']
        d1['typename']=d['TypeName']
        d1['units']=d['DefaultUnits']
        d1['author']=d['Author']
        d1['notes']=d['Notes']
        d1['quality']=d['DataQuality']
        d1['relevance']=d['DataRelevance']
        d1['data']=d['Documentation']
        d1['retionality']=d['Rationality']
    
        for j in range(0,len(y)):
            y[j]['No']=j+1
            y[j]['name']=l[j]['Name']
            y[j]['description']=l[j]['Description']
            y[j]['DamageImageName']=l[j]['DamageImageName']
            y[j]['median']=l[j]['Median']
            y[j]['dispersion']=l[j]['Beta']
            y[j]['RepairMeasures']=l[j]['RepairMeasures']
            y[j]['UseCasualty']=l[j]['UseCasualty']
            y[j]['LongLeadFlag']=l[j]['LongLeadFlag']
            y[j]['AffectedFloorArea']=l[j]['AffectedFloorArea']
            y[j]['AffectedDeathRate']=l[j]['AffectedDeathRate']
            y[j]['AffectedInjuryRate']=l[j]['AffectedInjuryRate']
            y[j]['AffectedDeathRateBeta']=l[j]['AffectedDeathRateBeta']
            y[j]['AffectedInjuryRateBeta']=l[j]['AffectedInjuryRateBeta']
            y[j]['RedTagMedian']=l[j]['RedTagMedian']
            y[j]['RedTagBeta']=l[j]['RedTagBeta']

            re_cost['l_Quantity']=d['DamageStates'][j]['CostConsequence']['LowerQuantity']
            re_cost['aver_re_l']=d['DamageStates'][j]['CostConsequence']['MaxAmount']
            re_cost['u_Quantity']=d['DamageStates'][j]['CostConsequence']['UpperQuantity']
            re_cost['aver_re_u']=d['DamageStates'][j]['CostConsequence']['MinAmount']
            re_cost['COV']=d['DamageStates'][j]['CostConsequence']['Uncertainty']
            re_cost['CurveType']=d['DamageStates'][j]['CostConsequence']['CurveType']

            re_time['l_Quantity']=d['DamageStates'][j]['TimeConsequence']['LowerQuantity']
            re_time['aver_re_l']=d['DamageStates'][j]['TimeConsequence']['MaxAmount']
            re_time['u_Quantity']=d['DamageStates'][j]['TimeConsequence']['UpperQuantity']
            re_time['aver_re_u']=d['DamageStates'][j]['TimeConsequence']['MinAmount']
            re_time['COV']=d['DamageStates'][j]['TimeConsequence']['Uncertainty']
            re_time['CurveType']=d['DamageStates'][j]['TimeConsequence']['CurveType']

            y[j]['CostConsequence']=re_cost
            y[j]['TimeConsequence']=re_time

        d1['DamageStates']=y
        return d1
    except Exception as e:
        return(str(e))
        
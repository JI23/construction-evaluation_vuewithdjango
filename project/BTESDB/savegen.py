import ast
from django.db.models import Max,Min,Sum
import os
from .models import DB_part,User_Info
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def savegen_gen_info(request):
    response={}
    print('333')
    part_id=request.GET['part_id']
    #print(part_id)
    gen_info=request.GET['gen_info']
    #print(type(gen_info))
    #print(gen_info)   
    #将string转化为dict
    gen_info=ast.literal_eval(gen_info)
    #print(type(gen_info))

    username=request.GET['username']
    this_user=User_Info.objects.get(username=username)
    first=gen_info['id'].split('.')[0]
    if len(gen_info['id'])==0:
        response['error_num']=1
        response['msg']='ID名不能为空'
        return JsonResponse(response)
    elif not DB_part.objects.filter(part_id__startswith=first).exists():
        response['error_num']=1
        response['msg']='ID名非法'
        return JsonResponse(response)
    elif DB_part.objects.filter(user=this_user,part_id=gen_info['id']).exists() and part_id==0:
        response['error_num']=1
        response['msg']='ID名不能重名'
        return JsonResponse(response)
    

    if DB_part.objects.filter(id=part_id).exists():
        #print('数据库中已存在')
        this_part=DB_part.objects.get(id=part_id)
        path='user_defined/'+username+'/'+gen_info['id']+'/'+gen_info['id']+'.xml'

        #print (os.getcwd())
        #print (os.listdir('./media/user_defined/'+username+'/'))
        old_path=r'./media/user_defined/'+username+r'/'
        if this_part.part_id!=gen_info['id']:
            if this_part.part_id in os.listdir(old_path):
                os.rename(old_path+this_part.part_id,old_path+gen_info['id'])
            if this_part.part_id+'.xml' in os.listdir(old_path+gen_info['id']+r'/'):
                os.rename(old_path+gen_info['id']+r'/'+this_part.part_id+'.xml',
                old_path+gen_info['id']+r'/'+gen_info['id']+'.xml')
            #print('文件及文件夹名修改成功')
        this_part.part_id=gen_info['id']
        this_part.part_name=gen_info['name']
        this_part.EDP_type='A'
        this_part.description=gen_info['description']
        this_part.xml=path
        try:
            #修改数据库内容并去修改xml
            this_part.save()
            path='user_defined/'+username+'/'+gen_info['id']+'/'+gen_info['id']+'.xml'
            #print(path)
            update_gen(path,gen_info)
            #print('xml修改完毕')
            response['error_num']=0
            response['msg']='修改成功'
            print('!!!!!!!!!!!!!!!')
        except Exception as e:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #print(str(e))
            response['error_num']=1
            response['msg']=str(e)
    return JsonResponse(response)

def update_gen(path,gen_info):
    #path+...
    path='./media/'+path
    tree=ET.ElementTree(file=path)
    root=tree.getroot()

    ID=root.find('ID');ID.text=gen_info['id']
    Description=root.find('Description');Description.text=gen_info['description']
    Name=root.find('Name');Name.text=gen_info['name']
    Correlation=root.find('Correlation');Correlation.text=gen_info['choose2']
    Directional=root.find('Directional');Directional.text=gen_info['choose1']
    Approved=root.find('Approved');Approved.text=gen_info['value2']
    UseEDPValueOfFloorAbove=root.find('UseEDPValueOfFloorAbove');UseEDPValueOfFloorAbove.text=gen_info['value1']

    EDPType=root.find('EDPType')
    Dimension=EDPType.find('Dimension');Dimension.text=gen_info['DP_Dimension']
    TypeName=EDPType.find('TypeName');TypeName.text=gen_info['typename']
    DefaultUnits=EDPType.find('DefaultUnits');DefaultUnits.text=str(gen_info['units'])
    
    tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")

def update_notes(path,notes_info):
    #path+...
    path='./media/'+path
    tree=ET.ElementTree(file=path)
    root=tree.getroot()

    Author=root.find('Author');Author.text=notes_info['author']
    Notes=root.find('Notes');Notes.text=notes_info['notes']

    Ratings=root.find('Ratings')
    DataQuality=Ratings.find('DataQuality');DataQuality.text=notes_info['quality']
    DataRelevance=Ratings.find('DataRelevance');DataRelevance.text=notes_info['relevance']
    Documentation=Ratings.find('Documentation');Documentation.text=notes_info['data']
    Rationality=Ratings.find('Rationality');Rationality.text=notes_info['rationality']

    tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")

def savegen(request):
    response={}
    part_id=request.GET['part_id']
    print(part_id)
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
   

    
    this_user=User_Info.objects.get(username=username)
    path='user_defined/'+username+'/'+gen_info['id']+'/'+gen_info['id']+'.xml'
    if DB_part.objects.filter(id=part_id).exists():
        print('数据库中已存在')
        this_part=DB_part.objects.get(id=part_id)
        path='user_defined/'+username+'/'+gen_info['id']+'/'+gen_info['id']+'.xml'
        this_part.data_resource=notes_info['author']
        this_part.save()
        update_notes(path,notes_info)
        #修改成功
        response['path2']=DB_part.objects.get(user=this_user,part_id=gen_info['id']).xml.url
        response['path']='media/user_defined/'+username+'/'+gen_info['id']+'/'
        response['part_id']=DB_part.objects.get(user=this_user,part_id=gen_info['id']).id
        response['error_num']=0
        response['msg']='数据库中已存在,修改成功'
    else:
        #到数据库中新建
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
        #调用此函数，生成xml文件，保存在media/user_defined文件夹下
        addDBpart(gen_info,notes_info,username)
        print('xml新建成功')
        #新建成功
        response['part_id']=DB_part.objects.get(user=this_user,part_id=gen_info['id']).id
        response['msg']='保存成功'
        response['error_num']=0
        response['path2']=DB_part.objects.get(user=this_user,part_id=gen_info['id']).xml.url
        response['path']='media/user_defined/'+username+'/'+gen_info['id']+'/'
    return JsonResponse(response)

import xml.etree.ElementTree as ET
import os
from datetime import datetime
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
    DateCreated=ET.SubElement(root,'DateCreated');DateCreated.text=datetime.now()
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

def savegen_num(request):
    print('savegen_num')
    response={}
    try:
        #获取数据
        path=request.GET['path']
        username=request.GET['username']
        statenum=request.GET['statenum']
        statenum=statenum[1:-1].split(' ')
        statenum=statenum[-1]

        statenum_info=request.GET['statenum_info']
        print(type(statenum_info))
        print(statenum_info)   
        #将string转化为dict
        statenum_info=ast.literal_eval(statenum_info)
        print(type(statenum_info))

        re_info=request.GET['re_info']
        print(type(re_info))
        print(re_info)   
        #将string转化为dict
        re_info=ast.literal_eval(re_info)
        print(type(re_info))

        re_cost=request.GET['re_cost']
        print(type(re_cost))
        print(re_cost)   
        #将string转化为dict
        re_cost=ast.literal_eval(re_cost)
        print(type(re_cost))

        re_time=request.GET['re_time']
        print(type(re_time))
        print(re_time)   
        #将string转化为dict
        re_time=ast.literal_eval(re_time)
        print(type(re_time))

        others=request.GET['others']
        #others.replace('false','0')
        #others.replace('true','1')
        print(type(others))
        print(others)   
        #将string转化为dict
        others=json.loads(others)
        #others=ast.literal_eval(others)
        print(others)
        print(type(others))
        
        

        #调用函数，添加损伤详情
        if addDamageState(path,statenum,statenum_info,re_info,re_cost,re_time,others):
            print('添加成功')
            response['error_num']=0
            response['msg']='损伤状态存储成功'
        else:
            print('others修改成功')
            response['error_num']=0
            response['msg']='others修改成功'
    except Exception as e:
        print (str(e))
        response['error_num']=1
        response['msg']='损伤状态存储失败'

    return JsonResponse(response)
def addDamageState(path,No,statenum_info,re_info,re_cost,re_time,others):
    print('addDamageState')
    n=path.split('/')[-2]+'.xml'
    path=path+n
    print(path)

    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    DamageStates=root.find('DamageStates')
    for subElement in DamageStates.findall('DamageState'):
        print('find')
        if subElement.attrib['No']==str(No):
            DamageState=subElement
            print("DamageState已存在")
            ConsequenceGroup=DamageState.find('ConsequenceGroup')
            UseCasualty=ConsequenceGroup.find('UseCasualty');UseCasualty.text=others['UseCasualty']
            LongLeadFlag=ConsequenceGroup.find('LongLeadFlag');LongLeadFlag.text=others['LongLeadFlag']
            AffectedFloorArea=ConsequenceGroup.find('AffectedFloorArea');AffectedFloorArea.text=others['AffectedFloorArea']
            AffectedDeathRate=ConsequenceGroup.find('AffectedDeathRate');AffectedDeathRate.text=others['AffectedDeathRate']
            AffectedInjuryRate=ConsequenceGroup.find('AffectedInjuryRate');AffectedInjuryRate.text=others['AffectedInjuryRate']
            AffectedDeathRateBeta=ConsequenceGroup.find('AffectedDeathRateBeta');AffectedDeathRateBeta.text=others['AffectedDeathRateBeta']
            AffectedInjuryRateBeta=ConsequenceGroup.find('AffectedInjuryRateBeta');AffectedInjuryRateBeta.text=others['AffectedInjuryRateBeta']
            RedTagMedian=ConsequenceGroup.find('RedTagMedian');RedTagMedian.text=others['RedTagMedian']
            RedTagBeta=ConsequenceGroup.find('RedTagBeta');RedTagBeta.text=others['RedTagBeta']

            tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")
            print('others修改完毕')
            return False
    else:
        print(DamageStates)
        
        DamageState=ET.SubElement(DamageStates,'DamageState',{'No':str(No)})
        Name=ET.SubElement(DamageState,'Name');Name.text=statenum_info['name']
        Description=ET.SubElement(DamageState,'Description');Description.text=statenum_info['description']
        DamageImageName=ET.SubElement(DamageState,'DamageImageName');DamageImageName.text=statenum_info['DamageImageName']
        ConsequenceGroup=ET.SubElement(DamageState,'ConsequenceGroup')
        RepairMeasures=ET.SubElement(ConsequenceGroup,'RepairMeasures');RepairMeasures.text=re_info['reInfo']
        TagState=ET.SubElement(ConsequenceGroup,'TagState');TagState.text=''
        UseCasualty=ET.SubElement(ConsequenceGroup,'UseCasualty');UseCasualty.text=others['UseCasualty']
        LongLeadFlag=ET.SubElement(ConsequenceGroup,'LongLeadFlag');LongLeadFlag.text=others['LongLeadFlag']
        AffectedFloorArea=ET.SubElement(ConsequenceGroup,'AffectedFloorArea');AffectedFloorArea.text=others['AffectedFloorArea']
        AffectedDeathRate=ET.SubElement(ConsequenceGroup,'AffectedDeathRate');AffectedDeathRate.text=others['AffectedDeathRate']
        AffectedInjuryRate=ET.SubElement(ConsequenceGroup,'AffectedInjuryRate');AffectedInjuryRate.text=others['AffectedInjuryRate']
        AffectedDeathRateBeta=ET.SubElement(ConsequenceGroup,'AffectedDeathRateBeta');AffectedDeathRateBeta.text=others['AffectedDeathRateBeta']
        AffectedInjuryRateBeta=ET.SubElement(ConsequenceGroup,'AffectedInjuryRateBeta');AffectedInjuryRateBeta.text=others['AffectedInjuryRateBeta']
        RedTagMedian=ET.SubElement(ConsequenceGroup,'RedTagMedian');RedTagMedian.text=others['RedTagMedian']
        RedTagBeta=ET.SubElement(ConsequenceGroup,'RedTagBeta');RedTagBeta.text=others['RedTagBeta']

        CostConsequence=ET.SubElement(ConsequenceGroup,'CostConsequence')
        LowerQuantity=ET.SubElement(CostConsequence,'LowerQuantity');LowerQuantity.text=re_cost['l_Quantity']
        MaxAmount=ET.SubElement(CostConsequence,'MaxAmount');MaxAmount.text=re_cost['aver_re_l']
        UpperQuantity=ET.SubElement(CostConsequence,'UpperQuantity');UpperQuantity.text=re_cost['u_Quantity']
        MinAmount=ET.SubElement(CostConsequence,'MinAmount');MinAmount.text=re_cost['aver_re_u']
        Uncertainty=ET.SubElement(CostConsequence,'Uncertainty');Uncertainty.text=re_cost['COV']
        CurveType=ET.SubElement(CostConsequence,'CurveType');CurveType.text=re_cost['CurveType']
        CostRatio=ET.SubElement(CostConsequence,'CostRatio');CostRatio.text=''
        RepairRatio=ET.SubElement(CostConsequence,'RepairRatio');RepairRatio.text=''
        LowerQuantityRatio=ET.SubElement(CostConsequence,'LowerQuantityRatio');LowerQuantityRatio.text=''
        UpperQuantityRatio=ET.SubElement(CostConsequence,'UpperQuantityRatio');UpperQuantityRatio.text=''

        TimeConsequence=ET.SubElement(ConsequenceGroup,'TimeConsequence')
        LowerQuantity=ET.SubElement(TimeConsequence,'LowerQuantity');LowerQuantity.text=re_time['l_Quantity']
        MaxAmount=ET.SubElement(TimeConsequence,'MaxAmount');MaxAmount.text=re_time['aver_re_l']
        UpperQuantity=ET.SubElement(TimeConsequence,'UpperQuantity');UpperQuantity.text=re_time['u_Quantity']
        MinAmount=ET.SubElement(TimeConsequence,'MinAmount');MinAmount.text=re_time['aver_re_u']
        Uncertainty=ET.SubElement(TimeConsequence,'Uncertainty');Uncertainty.text=re_time['COV']
        CurveType=ET.SubElement(TimeConsequence,'CurveType');CurveType.text=re_time['CurveType']
        LowerQuantityRatio=ET.SubElement(TimeConsequence,'LowerQuantityRatio');LowerQuantityRatio.text=''
        UpperQuantityRatio=ET.SubElement(TimeConsequence,'UpperQuantityRatio');UpperQuantityRatio.text=''

        Median=ET.SubElement(DamageState,'Median');Median.text=statenum_info['median']
        Beta=ET.SubElement(DamageState,'Beta');Beta.text=statenum_info['dispersion']

        print('end')
        print(type(path))
        tree.write(path)
        return True

            
            
  

import os
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def savegen_image(request):
    print('savegen_image')
    response={}
    try:
        #获取数据
        image=request.FILES.get('image')
        path=request.POST['path']
        num=request.POST['statenum']
        num=num.replace('"','')
        num=num.split(' ')[-1]
        print(image.name)
        print(path)
        print(num)
        if image.name.endswith('.jpg') or image.name.endswith('.png') or image.name.endswith('.JPG') or image.name.endswith('.PNG'):
            print('是图片')
        else:
            response['error_num']=1
            response['msg']='只能上传jpg/png文件！'
            return JsonResponse(response)
        #检验路径合理性
        folder=os.path.exists(path)
        if not folder:
            print('图片路径有误')
            response['error_num']=1
            response['msg']='图片存放路径有误'
            return JsonResponse(response)
        else:
            #若存在同名称的图片，先将其删除
            if os.path.exists(path+str(num)+'_'+image.name):
                print('存在同名图片')
                os.remove(path+str(num)+'_'+image.name)
            with open(path+str(num)+'_'+image.name,'wb+') as dest:
                for chunk in image.chunks():      # 分块写入文件
                    dest.write(chunk)
            print('图片存放成功')
            print('图片路径为：'+path+str(num)+'_'+image.name)
    except Exception as e:
        print (str(e))
        response['error_num']=1
        response['msg']='图片上传出现问题'

    return JsonResponse(response)
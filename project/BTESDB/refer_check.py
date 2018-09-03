import ast
import json
from django.http import JsonResponse
import os
import xml.etree.ElementTree as ET
def update_statenum(path,No,statenum_info):
    print('update_statenum')
    #path+...
    path=path+path.split('/')[-2]+'.xml'
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    DamageStates=root.find('DamageStates')

    print('开始修改')
    for subElement in DamageStates.findall('DamageState'):
        if subElement.attrib['No']==str(No):
            DamageState=subElement  # 使用Element.find()

            Name=DamageState.find('Name');Name.text=statenum_info['name']
            Description=DamageState.find('Description');Description.text=statenum_info['description']
            DamageImageName=DamageState.find('DamageImageName');DamageImageName.text=statenum_info['DamageImageName']
            Median=DamageState.find('Median');Median.text=statenum_info['median']
            Beta=DamageState.find('Beta');Beta.text=statenum_info['dispersion']

            tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")

def refer_check_statenum(request):
    print('refer_check_statenum')
    response={}
    try:
        #获取数据
        statenum=request.GET['statenum']
        statenum=statenum[1:-1].split(' ')
        statenum=statenum[-1]
        print(statenum)
        statenum_info=request.GET['statenum_info']
        statenum_info=ast.literal_eval(statenum_info)
        path=request.GET['path']
        path='./'+path
        folder=os.path.exists(path)
        if not folder:
            response['error_num']=1
            response['msg']='文件路径有误！'
            return JsonResponse(response)
        else:
            for each in os.listdir(path):
                print(each)
                if each.startswith(statenum+'_'):
                    print('获取图片地址成功')
                    response['DamageImageName']=path+each
                    break
            else:
                print('无对应图片')
                response['DamageImageName']='null'

        #检验数据合理性
        if len(statenum_info['name'])==0:
            response['error_num']=1
            response['msg']='损伤状态名称不能为空'
            return JsonResponse(response)
        
        try:
            statenum_info['median']=float(statenum_info['median'])
        except Exception as e:
            print(str(e))
            response['error_num']=1
            response['msg']='中位值必须为实数'
            return JsonResponse(response)

        try:
            statenum_info['dispersion']=float(statenum_info['dispersion'])
        except Exception as e:
            print(str(e))
            response['error_num']=1
            response['msg']='dispersion必须为实数'
            return JsonResponse(response)
        
        if len(statenum_info['description'])==0:
            response['error_num']=1
            response['msg']='损伤状态描述不能为空'
            return JsonResponse(response)
        
        update_statenum(path,statenum,statenum_info)
        print('xml修改完毕')

        response['error_num']=0
        response['msg']='存储成功'
    except Exception as e:
        print(str(e))
        response['error_num']=1
        response['msg']='易损件详情有误'
    return JsonResponse(response)

def update_re(path,No,re_info):
    #path+...
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    DamageStates=root.find('DamageStates')
    print(re_info)
    print(type(re_info))
    for subElement in DamageStates.findall('DamageState'):
        if subElement.attrib['No']==str(No):
            print(subElement.attrib['No'])
            print(No)
            DamageState=subElement  # 使用Element.find()
            ConsequenceGroup=DamageState.find('ConsequenceGroup')
            RepairMeasures=ConsequenceGroup.find('RepairMeasures');RepairMeasures.text=re_info
            
            tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")
            print('re_info修改完毕')
            return True
    else:
        return False

def refer_check_re_info(request):
    print('refer_check_re_info')
    response={}
    try:
        #获取数据
        re_info=request.GET['re_info']
        print(re_info)
        path="."+request.GET['path']
        print(path)
        statenum=request.GET['statenum']
        statenum=statenum[1:-1].split(' ')
        statenum=statenum[-1]
        print(statenum)
        if len(re_info)==0:
            response['error_num']=1
            response['msg']='修理信息不能为空'
            return JsonResponse(response)
        if update_re(path,statenum,re_info):
            print('修理信息修改成功')
            response['error_num']=0
            response['msg']='修理信息修改成功'
            return JsonResponse(response) 
        response['error_num']=0
        response['msg']='下一步'  
    except Exception as e:
        print(str(e))
        response['error_num']=1
        response['msg']='修理信息有误'
    return JsonResponse(response)

def is_int(a):
    try:
        a=int(a)
        return True
    except Exception as e:
        print (str(e))
        return False
def is_float(a):
    try:
        a=float(a)
        return True
    except Exception as e:
        print(str(e))
        return False

def refer_check_re_costAndTime(request):
    print('refer_check_re_cost')
    response={}
    try:
        #获取数据
        path="."+request.GET['path']
        print(path)
        statenum=request.GET['statenum']
        statenum=statenum[1:-1].split(' ')
        statenum=statenum[-1]
        print(statenum)
        flag=request.GET['flag']
        re_cost=request.GET['re_cost']
        re_cost=ast.literal_eval(re_cost)
        print(re_cost)
        print(type(re_cost))
        #检验数据合理性
        if not is_int(re_cost['l_Quantity']):
            response['error_num']=1
            response['msg']='LowerQuantity必须为整数'
            return JsonResponse(response)
        if not is_float(re_cost['aver_re_l']):
            response['error_num']=1
            response['msg']='Average Repair Cost for Lower Quantity必须为实数'
            return JsonResponse(response)
        if not is_int(re_cost['u_Quantity']):
            response['error_num']=1
            response['msg']='UpperQuantity必须为整数'
            return JsonResponse(response)
        if not is_float(re_cost['aver_re_u']):
            response['error_num']=1
            response['msg']='Average Repair Cost for Upper Quantity必须为实数'
            return JsonResponse(response)
        if not is_float(re_cost['COV']):
            response['error_num']=1
            response['msg']='COV必须为实数！'
            return JsonResponse(response)
        if flag=='cost':
            if update_cost(path,statenum,re_cost):
                response['error_num']=0
                response['msg']='re_cost修改成功'
                return JsonResponse(response)
        elif flag=='time':
            if update_time(path,statenum,re_cost):
                response['error_num']=0
                response['msg']='re_time修改成功'
                return JsonResponse(response)
        response['error_num']=0
        response['msg']='下一步'
        return JsonResponse(response)       
    except:
        response['error_num']=1
        response['msg']='数据获取失败'
    return JsonResponse(response)

def update_cost(path,No,re_cost):
    #path+...
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    DamageStates=root.find('DamageStates')

    for subElement in DamageStates.findall('DamageState'):
        if subElement.attrib['No']==str(No):
            DamageState=subElement 
            ConsequenceGroup=DamageState.find('ConsequenceGroup')
            CostConsequence=ConsequenceGroup.find('CostConsequence')

            LowerQuantity=CostConsequence.find('LowerQuantity');LowerQuantity.text=re_cost['l_Quantity']
            MaxAmount=CostConsequence.find('MaxAmount');MaxAmount.text=re_cost['aver_re_l']
            UpperQuantity=CostConsequence.find('UpperQuantity');UpperQuantity.text=re_cost['u_Quantity']
            MinAmount=CostConsequence.find('MinAmount');MinAmount.text=re_cost['aver_re_u']
            Uncertainty=CostConsequence.find('Uncertainty');Uncertainty.text=re_cost['COV']
            CurveType=CostConsequence.find('CurveType');CurveType.text=re_cost['CurveType']

            tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")
            print('re_cost修改成功')
            return True
    else:
        return False

def update_time(path,No,re_time):
    #path+...
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    DamageStates=root.find('DamageStates')

    for subElement in DamageStates.findall('DamageState'):
        if subElement.attrib['No']==str(No):
            DamageState=subElement 
            ConsequenceGroup=DamageState.find('ConsequenceGroup')
            TimeConsequence=ConsequenceGroup.find('TimeConsequence')

            LowerQuantity=TimeConsequence.find('LowerQuantity');LowerQuantity.text=re_time['l_Quantity']
            MaxAmount=TimeConsequence.find('MaxAmount');MaxAmount.text=re_time['aver_re_l']
            UpperQuantity=TimeConsequence.find('UpperQuantity');UpperQuantity.text=re_time['u_Quantity']
            MinAmount=TimeConsequence.find('MinAmount');MinAmount.text=re_time['aver_re_u']
            Uncertainty=TimeConsequence.find('Uncertainty');Uncertainty.text=re_time['COV']
            CurveType=TimeConsequence.find('CurveType');CurveType.text=re_time['CurveType']

            tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")
            print('re_time修改成功')
            return True
    else:
        return False

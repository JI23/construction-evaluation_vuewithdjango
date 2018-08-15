from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单
from django.utils import timezone

class One_Project_Form(forms.Form):
    '''项目信息'''
    project_name=forms.CharField(label='项目名称',max_length=45,help_text='总字数不可超过45',required=True,
    error_messages={'required':"Please enter the project's name",'max_length':'最大长度为45'})
    client_name=forms.CharField(label='客户名称',max_length=45,help_text='总字数不可超过45',error_messages={'max_length':'最大长度为45'})
    project_description=forms.CharField(label='项目描述',max_length=300,help_text='总字数不可超过300',error_messages={'max_length':'最大长度为300'})
    project_leader=forms.CharField(label='项目负责人',max_length=100)
class Two_Project_Form(forms.Form):
    '''建筑信息'''
    material=forms.CharField(label='材料',max_length=30,help_text='总字数不可超过30',required=True,error_messages={'required':"Please enter the project's materiral",'max_length':'最大长度为30'})
    structure_type=forms.CharField(label='结构类型',max_length=20,help_text='总字数不可超过20',required=True,error_messages={'required':"Please enter the project's struture type",'max_length':'最大长度为20'})
    floor=forms.IntegerField(label='楼层数')
    figure_time=forms.DateField(label='图审时间',help_text='需大于项目创建时间,形如：2018-8-12')#第一种方法
    #第二种方法，转换类型   将三个分别代表年月日的charfiled类型合并转换成datefiled
    #figure_time_year=forms.CharField(label='',max_length=4,min_length=2,help_text='形如：2018'，required=True,error_messages={'required':"请输入图审时间的年份",'max_lenth':"最大长度为4",'min_length':"最小长度为2"})
    height=forms.DecimalField(label='楼层总高',max_digits=5,decimal_places=2,help_text='取值范围为0-999.99',error_messages={'max_value':'最大值为999.99','min_value':'最小值为0'})
    area=forms.DecimalField(label='总面积',max_digits=7,decimal_places=2,help_text='取值范围为0-99999.99',error_messages={'max_value':'最大值为99999.99','min_value':'最小值为0'})
    cost_per_squaremeter=forms.DecimalField(label='每平米造价',max_digits=7,decimal_places=2,help_text='取值范围为0-99999.99',error_messages={'max_value':'最大值为99999.99','min_value':'最小值为0'})
    

def one_project(request):
    print(1)
    username=request.session['username']
    if request.method=='POST':
        print(2)
        pf=One_Project_Form(request.POST)
        if pf.is_valid():
            #获取表单数据
            print(3)
            project_name=pf.cleaned_data['project_name']
            client_name=pf.cleaned_data['client_name']
            project_description=pf.cleaned_data['project_description']
            project_leader=pf.cleaned_data['project_leader']
            

            #获取user外键
            this_user=User_Info.objects.get(username=username)
            
            request.session['project_name']=project_name
            request.session['client_name']=client_name
            request.session['project_description']=project_description
            request.session['project_leader']=project_leader

            
            print(4)
            print (username)
            #return HttpResponse('<p>数据添加成功</p>')
            return render(request,'new_project.html',{'pf':pf,'project_error':'数据添加成功'})

        else:
            print(5)
            return render(request,'new_project.html',{'pf':pf,'project_error':'有误！'})

    else:
        print(6)
        pf=One_Project_Form()
    return render(request,'new_project.html',{'pf':pf})

def two_project(request):
    print(1)
    username=request.session['username']
    
    
    if request.method=='POST':
        print(2)
        pf=Two_Project_Form(request.POST)
        if pf.is_valid():
            #获取表单数据
            print(3)
            create_time=timezone.now().strftime("%Y-%m-%d")

            material=pf.cleaned_data['material']
            structure_type=pf.cleaned_data['structure_type']
            floor=pf.cleaned_data['floor']
            figure_time=pf.cleaned_data['figure_time']
            height=pf.cleaned_data['height']
            area=pf.cleaned_data['area']
            cost_per_squaremeter=pf.cleaned_data['cost_per_squaremeter']

            request.session['floor']=floor
            request.session['floor_now']=1
            
            project_name=request.session['project_name']
            client_name=request.session['client_name']
            project_description=request.session['project_description']
            project_leader=request.session['project_leader']
            print(project_name)

            #获取user外键
            this_user=User_Info.objects.get(username=username)

            new=Project(user=this_user,
            project_name=project_name,
            client_name=client_name,
            project_description=project_description,
            create_time=create_time,
            project_leader=project_leader,
            material=material,
            structure_type=structure_type,
            floor=floor,
            figure_time=figure_time,
            height=height,
            area=area,
            cost_per_squaremeter=cost_per_squaremeter,
            is_finished=False,
            rate='0')
            new.save()

            request.session['project']=new.id
            print(4)
            print (username)
            print (project_name)
            return render(request,'new_project2.html',{'pf':pf,'project_error':'数据添加成功'})

        else:
            print(5)
            return render(request,'new_project2.html',{'pf':pf,'project_error':'有误！'})

    else:
        print(6)
        pf=Two_Project_Form()
    return render(request,'new_project2.html',{'pf':pf})


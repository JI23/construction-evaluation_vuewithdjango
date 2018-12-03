from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单
from django.contrib.auth.models import User   #导入django自带的user表
from django.http import JsonResponse

class User_Register_Form(forms.Form):
    #用户注册表单
    username=forms.CharField(label='手机号（用户名）',max_length=11,required=True)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
    password_again=forms.CharField(label='再次输入密码',widget=forms.PasswordInput())
    email=forms.EmailField(label='邮箱')
    truename=forms.CharField(label='真实姓名',max_length=20)
    nickname=forms.CharField(label='昵称',max_length=20)   
    architect_id=forms.CharField(label='建筑师证号',max_length=12,required=False)
    
    com_name=forms.CharField(label='公司名',max_length=60)
    certificate=forms.CharField(label='公司税号',max_length=18)
    job=forms.CharField(label='职务',max_length=20,required=False)
    #com_tel=forms.CharField(label='公司电话',max_length=13,)
    #fax=forms.CharField(label='传真号',max_length=13)
    #address=forms.CharField(label='地址',max_length=100)
    #com_tel=request.POST['com_tel']
    #fax=request.POST['fax']
    #address=request.POST['address']

# Create your views here.   

def user_register(request):
    if request.method=='GET':
        response={}
        #获取表单数据
        com_name=request.GET['com_name']
        certificate=request.GET['certificate']
        job=request.GET['job']
        com_exist=Company_Info.objects.filter(certificate=certificate,com_name=com_name)
        #验证是否存在该公司，若不存在，在company_info新增一条公司条目
        #验证是否存在该公司，若不存在，不可以申请成为用户
        '''
        if not com_exist.exists():
            new=Company_Info(com_name=com_name,certificate=certificate)
            new.save()
             this_company=Company_Info.objects.filter(certificate=certificate)
         '''

        if not com_exist.exists():
            #公司不在数据库中
            response['error_num']=1
            response['msg']='公司不在数据库中！'
            return JsonResponse(response)
               #return render(request,'user_register.html', {'uf': uf,'user_register_error':'公司不存在'})
        else:
                #
            username = request.GET['username']
            telephone=request.GET['username']  
            password = request.GET['password']
            password_again=request.GET['password_again']
            email=request.GET['email']
            nickname=request.GET['nickname']
            truename=request.GET['truename']
            architect_id=request.GET['architect_id']
            job=request.GET['job']
            if str(password)==str(password_again):
                    #两次密码相同，尝试添加到数据库
                try:
                    print('密码相同')
                    registAdd = User_Info.objects.create_user(username=username, password=password,login_amount=0,company=com_exist[0],
                    telephone=telephone,email=email,nickname=nickname,truename=truename,architect_id=architect_id,job=job,
                    is_superuser=False,is_staff=False, is_active=True) 
                    #添加成功   
                    #return render(request,'fail_user.html', {'registAdd': '管理员'+username})
                    response['error_num']=0
                    response['msg']='注册成功'
                    return JsonResponse(response)
                except Exception:
                    #添加失败
                    #return render(request,'fail_user.html', {'registAdd': '注册失败', 'username': username,'architect_id':architect_id})
                    response['error_num']=1
                    response['msg']='添加失败'
                    return JsonResponse(response)
            else:
                #两次密码不同
                #uf.clean()
                response['error_num']=1
                response['msg']='两次密码必须相同！'
                return JsonResponse(response)
                    #return render(request,'user_register.html', {'uf': uf,'user_register_error':'两次密码不一样'})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
       return JsonResponse(response)
    #return render(request,'user_register.html', {'uf': uf})



class Admin_Register_Form(forms.Form):
    #管理员注册表单
    username=forms.CharField(label='手机号（用户名）',max_length=11,required=True)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
    password_again=forms.CharField(label='再次输入密码',widget=forms.PasswordInput())
    email=forms.EmailField(label='邮箱')
    truename=forms.CharField(label='真实姓名',max_length=20)
    nickname=forms.CharField(label='昵称',max_length=20)   
    architect_id=forms.CharField(label='建筑师证号',max_length=12,required=False)
    
    com_name=forms.CharField(label='公司名',max_length=60)
    certificate=forms.CharField(label='公司税号',max_length=18)
    job=forms.CharField(label='职务',max_length=20,required=False)
    com_tel=forms.CharField(label='公司电话',max_length=13,)
    fax=forms.CharField(label='传真号',max_length=13)
    address=forms.CharField(label='地址',max_length=100)
   

def admin_register(request):
    if request.method=='POST':
        response={}
        #包含用户注册的一些必要信息，如user_register_form所示
        uf=Admin_Register_Form(request.POST) 
        print (1)
        if uf.is_valid():
            #获取表单数据
            print(2)
            com_name=request.POST['com_name']
            certificate=request.POST['certificate']
            job=request.POST['job']
            com_tel=request.POST['com_tel']
            fax=request.POST['fax']
            address=request.POST['address']
            
            com_exist=Company_Info.objects.filter(certificate=certificate,com_name=com_name)
            
            #验证是否存在该公司，若不存在，不可以申请成为用户
            
            if not com_exist.exists():
                print (3)
                #验证是否存在该公司，若不存在，在company_info新增一条公司条目
                new=Company_Info(com_name=com_name,certificate=certificate,com_tel=com_tel,fax=fax,address=address,total_user=0)
                new.save()
                this_company=Company_Info.objects.get(certificate=certificate)
            else:
                this_company=com_exist[0]
            
            print(4)
            username = request.POST['username']
            telephone=request.POST['username']  
            password = request.POST['password']
            password_again=request.POST['password_again']
            email=request.POST['email']
            nickname=request.POST['nickname']
            truename=request.POST['truename']
            architect_id=request.POST['architect_id']
            if str(password)==str(password_again):
                #两次密码相同，尝试添加到数据库
                print (5)
                try:
                    registAdd = User_Info.objects.create_user(username=username, password=password,login_amount=0,company=this_company,
                    telephone=telephone,email=email,nickname=nickname,truename=truename,job=job,architect_id=architect_id,
                    is_superuser=True,is_staff=True, is_active=True) 
                    #添加成功   
                    return render(request,'fail_user.html', {'registAdd': '管理员'+username})
                    
                except Exception:
                    #添加失败
                    print(6)
                    return render(request,'fail_user.html', {'registAdd': '注册失败', 'username': username,'architect_id':architect_id})
                
            else:
                #两次密码不同
                print (7)
                return render(request,'user_register.html', {'uf': uf,'user_register_error':'两次密码不一样'})
                
    else:
        print(8)
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = Admin_Register_Form()
    return render(request,'user_register.html', {'uf': uf})


class Company_Register_Form(forms.Form): 
    #公司注册表单    
    com_name=forms.CharField(label='公司名',max_length=60)
    certificate=forms.CharField(label='公司税号',max_length=18)
    #job=forms.CharField(label='职务',max_length=20,required=False)
    com_tel=forms.CharField(label='公司电话',max_length=13,)
    fax=forms.CharField(label='传真号',max_length=13)
    address=forms.CharField(label='地址',max_length=100)

def company_register(request):
    if request.method=='POST':
        response={}
        #包含公司注册的一些必要信息，如company_register_form所示
        uf=Company_Register_Form(request.POST) 
        print (1)
        if uf.is_valid():
            #获取表单数据
            print(2)
            com_name=request.POST['com_name']
            certificate=request.POST['certificate']
            #job=request.POST['job']
            com_tel=request.POST['com_tel']
            fax=request.POST['fax']
            address=request.POST['address']
            
            com_exist=Company_Info.objects.filter(certificate=certificate,com_name=com_name)
            
            if not com_exist.exists():
                print (3)
                #验证是否存在该公司，若不存在，在company_info新增一条公司条目
                new=Company_Info(com_name=com_name,certificate=certificate,com_tel=com_tel,fax=fax,address=address,total_user=0)
                new.save()
                this_company = Company_Info.objects.filter(certificate=certificate)
                #return render(request,'fail_user.html', {'registAdd': '公司'+com_name})
                return JsonResponse(response)
            else:
                print(4)
                #公司存在
                #return render(request,'fail_user.html', {'registAdd': '注册失败', 'username': com_name})
                return JsonResponse(response)
    
                
    else:
        print(8)
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = Company_Register_Form()
    #return render(request,'user_register.html', {'uf': uf})
    return JsonResponse(response)

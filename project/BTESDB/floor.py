from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单

class Floor_Info_Form(forms.Form):
    '''楼层信息'''
    #floor_no=forms.IntegerField(label='第几层',help_text='不可超过总楼层数')
    floor_height=forms.DecimalField(label='楼层高度',max_digits=4,decimal_places=2,help_text='取值范围为0-99.99',error_messages={'max_value':'最大值为99.99','min_value':'最小值为0'})
    floor_area=forms.DecimalField(label='楼层面积',max_digits=6,decimal_places=2,help_text='取值范围为0-9999.99',error_messages={'max_value':'最大值为9999.99','min_value':'最小值为0'})
    influence_coefficient=forms.DecimalField(label='楼层影响系数',max_digits=5,decimal_places=4,help_text='取值范围为0-9.9999',error_messages={'max_value':'最大值为9.9999','min_value':'最小值为0'})
    population_density=forms.DecimalField(label='人口密度',max_digits=3,decimal_places=2,help_text='取值范围为0-9.99',error_messages={'max_value':'最大值为9.99','min_value':'最小值为0'})


def three_floor(request):
    project=request.session['project']
    username=request.session['username']
    floor= request.session['floor']
    floor_list=list()
    print (1)
    #获取user外键
    this_user=User_Info.objects.get(username=username)
    this_project=Project.objects.get(id=project)
    if request.method=='POST':
        print(2)
        print (request.POST)
        floor_list=request.POST
        floor_height_list=request.POST.getlist('floor_height',[])
        floor_area_list=request.POST.getlist('floor_area',[])
        influence_coefficient_list=request.POST.getlist('influence_coefficient',[])
        population_density_list=request.POST.getlist('population_density',[])
        for i in range (floor):

            new_floor=Floor_Info(project=this_project,
            #user=this_user,
            floor_no=i+1,
            floor_height=floor_area_list[i],
            floor_area=floor_area_list[i],
            influence_coefficient=influence_coefficient_list[i],
            population_density=population_density_list[i])
            new_floor.save()
        AddResponse='数据添加成功'
        return render(request,'new_project3.html',locals())
    else:
        print(4)
        for i in range(floor):
            floor_list.append(Floor_Info_Form())
    return render(request,'new_project3.html',{'floor_list':floor_list})
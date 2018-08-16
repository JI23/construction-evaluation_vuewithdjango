from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单
class Earthquake_Info_Form(forms.Form):
    '''地震信息'''
    defense_intensity_list=(
        ('6','6度'),
        ('7.1','7度(0.1g)'),
        ('7.15','7度(0.15g)'),
        ('8.2','8度(0.2g)'),
        ('8.3','8度(0.3g)'),
        ('9','9度'),
    )
    defense_intensity=forms.CharField(label='设防烈度',
    widget=forms.widgets.Select(choices=defense_intensity_list),initial='6度')
    site_classification_list={
        ('0','I_0'),
        ('1','I_1'),
        ('2','II'),
        ('3','III'),
        ('4','IV'),
    }
    site_type=forms.CharField(label='场地类别',widget=forms.Select(choices=site_classification_list),initial='I_0')
    number=forms.IntegerField(label='地震波数量')
    group_list={
        ('1','第一组'),
        ('2','第三组'),
        ('3','第二组'),
    }
    group=forms.CharField(label='地震分组',widget=forms.Select(choices=group_list),initial='第一组')
    earthquake_level_list={
        ('L','多遇地震'),
        ('M','设防地震'),
        ('S','罕遇地震'),
    }
    earthquake_level=forms.CharField(label='地震水准',widget=forms.Select(choices=earthquake_level_list),initial='多遇地震')

def earthquake_info(request):
    project=request.session['project']
    this_project=Project.objects.get(id=project)
    username=request.session['username']

    if request.method=='POST':
        print(2)
        print (request.POST)
        ef=Earthquake_Info_Form(request.POST)
        if ef.is_valid():
             #获取表单数据
            defense_intensity=ef.cleaned_data['defense_intensity']
            site_type=ef.cleaned_data['site_type']
            number=ef.cleaned_data['number']
            request.session['number']=number
            group=ef.cleaned_data['group']
            earthquake_level=ef.cleaned_data['earthquake_level']
            new=Earthquake_Info(project=this_project,
            defense_intensity=defense_intensity,
            site_type=site_type,
            number=number,
            group=group,
            earthquake_level=earthquake_level)
        AddResponse='数据添加成功'
        return render(request,'new_project6.html',locals())
    else:
        print(4)
        ef=Earthquake_Info_Form()
    return render(request,'new_project6.html',locals())
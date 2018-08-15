from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单

class Earthquake_wave_detail_Form(forms.Form):
    '''地震波详情'''
    #earthquake_wave_no=forms.IntegerField(label='地震波编号',help_text='不可超过地震波总数')
    earthquake_wave_name=forms.CharField(label='地震波名称',max_length=15,help_text='总字数不可超过15',error_messages={'max_length':'最大长度为15'})
    peak=forms.DecimalField(label='地震波峰值',max_digits=4,decimal_places=2,help_text='取值范围为0-99.99')
    earthquake_wave_file=forms.FileField(label='文件存放位置',allow_empty_file=False)
def wave_info(request):
    number=request.session['number']
    
    wave_list=list()
    if request.method=='POST':
        wave_list=request.POST
        print(request.POST)
        project=request.session['project']
        this_project=Project.objects.get(id=project)
        earthquake_wave_name_list=request.POST.getlist('earthquake_wave_name',[])
        peak_list=request.POST.getlist('peak',[])
        earthquake_wave_file_list=request.POST.getlist('earthquake_wave_file',[])
        for i in range(number):
            new=Earthquake_wave_detail(project=this_project,
            earthquake_wave_no=i+1,
            earthquake_wave_name=earthquake_wave_name_list[i],
            peak=peak_list[i],
            earthquake_wave_file=earthquake_wave_file_list[i])
            new.save()
        AddResponse='数据添加成功'
        return render(request,'new_project7.html',locals())
    else:
        for i in range(number):
            wave_list.append(Earthquake_wave_detail_Form)
        return render(request,'new_project7.html',locals())

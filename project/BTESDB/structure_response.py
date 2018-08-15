from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单
class Structure_response_Form(forms.Form):
    direction_list=(
        ('X','X'),
        ('Y','Y'),
    )
    direction=forms.CharField(label='方向',max_length=1,widget=forms.Select(choices=direction_list),initial='X')
    #EDP类型，分层间位移角和楼层加速度
    EDP_type_list=(
        ('S','Story Drift Ratio'),#层间位移角
        ('A','Acceleration'),#楼层加速度
    )
    EDP_type=forms.CharField(label='EDP类型',max_length=1,widget=forms.Select(choices=EDP_type_list),initial='S')
     #指向DB_type的外键，一个结构构件对应一个结构类型
    #楼层数量决定表的宽度，地震数量决定表的长度
    #floor_no=forms.IntegerField(label='楼层数量',help_text='需等于楼层总数')
    #earthquake_no=forms.IntegerField(label='地震数量',help_text='需等于地震波总数')
def structure_response(request):
    print(1)
    floor=request.session['floor']#楼层数
    number=request.session['number']#地震数
    if request.method=='POST':
        print(2)
        sf=Structure_response_Form(request.POST)
        if sf.is_valid():
            direction=sf.cleaned_data['direction']
            EDP_type=sf.cleaned_data['EDP_type']
            AddResponse='数据保存成功'
            return render(request,'new_project8.html',locals())
        else:
            AddResponse='有误!'
            return render(request,'new_project8.html',locals())
    else:
        print(3)
        sf=Structure_response_Form()
        return render(request,'new_project8.html',locals())
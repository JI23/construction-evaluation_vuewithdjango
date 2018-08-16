from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import auth
from django import forms    #导入表单
def get_all_parts(request):
    part_list = DB_part.objects.all()
    # print article_list
    # print type(article_list)
    #QuerySet是一个可遍历结构，包含一个或多个元素，每个元素都是一个Model实例
    #QuerySet类似于Python中的list，list的一些方法QuerySet也有，比如切片，遍历。
    #每个Model都有一个默认的manager实例，名为objects，QuerySet有两种来源：通过manager的方法得到、通过QuerySet的方法得到。mananger的方法和QuerySet的方法大部分同名，同意思，如filter(),update()等，但也有些不同，如manager有create()、get_or_create()，而QuerySet有delete()等
    #locals()返回一个包含当前作用域里面的所有变量和它们的值的字典。
    return render(request, 'all_part.html',{'part_list': part_list})

def show_selected_structure(request,id):
    print (1)
    if id == '0' :
        print (2)       
        selected_id_list=list()
        request.session['selected_id_list']=selected_id_list
        return render(request, 'new_project4.html')
    else:
        print (3)
        selected_id_list=request.session['selected_id_list']
        selected_id_list.append(id)
        request.session['selected_id_list']=selected_id_list
        print (selected_id_list)

        selected_list=list()
        for i in selected_id_list:
            get=DB_part.objects.get(id=int(i))
            print ( get )
            selected_list.append(get)
        print (selected_list)
        return render(request, 'new_project4.html',locals())

def show_selected_nonstructure(request,id):
    print (1)
    if id == '0' :
        print (2)        
        selected_id_list=list()
        request.session['selected_id_list']=selected_id_list
        return render(request, 'new_project5.html')
    else:
        print (3)
        selected_id_list=request.session['selected_id_list']
        selected_id_list.append(id)
        request.session['selected_id_list']=selected_id_list
        print (selected_id_list)

        selected_list=list()
        for i in selected_id_list:
            get=DB_part.objects.get(id=int(i))
            print ( get )
            selected_list.append(get)
        print (selected_list)
        return render(request, 'new_project5.html',locals())

def save_structure(request):
    if request.method=='POST':
        print (3)
        selected_id_list=request.session['selected_id_list']           
        start=request.POST.getlist('start',[])
        stop=request.POST.getlist('stop',[])
        project=request.session['project']
        this_project=Project.objects.get(id=project)
        index=0
        for i in selected_id_list:
            print(4)
            this_part=DB_part.objects.get(id=int(i))
            start_floor=start[index]
            stop_floor=stop[index]
            new=Element(project=this_project,
            element_type='s',
            element=this_part,
            start_floor=start_floor,
            stop_floor=stop_floor)
            new.save()
        print(5)
        AddResponse='数据添加成功'
        return render(request, 'new_project4.html',locals())
    else:
        Http404 

def save_nonstructure(request):
    if request.method=='POST':
        print (3)
        selected_id_list=request.session['selected_id_list']           
        start=request.POST.getlist('start',[])
        stop=request.POST.getlist('stop',[])
        project=request.session['project']
        this_project=Project.objects.get(id=project)
        index=0
        for i in selected_id_list:
            print(4)
            this_part=DB_part.objects.get(id=int(i))
            start_floor=start[index]
            stop_floor=stop[index]
            new=Element(project=this_project,
            element_type='s',
            element=this_part,
            start_floor=start_floor,
            stop_floor=stop_floor)
            new.save()
        print(5)
        AddResponse='数据添加成功'
        return render(request, 'new_project5.html',locals())
    else:
        Http404 
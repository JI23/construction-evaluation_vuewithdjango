

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import DB_part,Damage_state_detail,Damage_state_test
from django.contrib import auth
from django import forms    #导入表单
from django.contrib.auth.models import User   #导入django自带的user表
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt

def insert(request):
    get=Damage_state_test.objects.all()
    #print (get)
    for item in get:
        #print (item.DB_part)
        #print (len(item.DB_part))
        fk=DB_part.objects.get(part_id=item.DB_part)
        new=Damage_state_detail(DB_part=fk,
        damage_id=item.damage_id,
        damage_state=item.damage_state,
        damage_description=item.damage_description,
        median=item.median,
        variance=item.variance,
        lost_parameter=item.lost_parameter,
        rehabilitation_coeffcient=item.rehabilitation_coeffcient,
        min_rehab_cost=item.min_rehab_cost,
        min_lost_cost=item.min_lost_cost,
        max_rehab_cost=item.max_rehab_cost,
        max_lost_cost=item.max_lost_cost,
        cov_cost=item.cov_cost,
        repair_people_day=item.repair_people_day,
        min_rehab_time=item.min_rehab_time,
        min_lost_time=item.min_lost_time,
        max_rehab_time=item.max_rehab_time,
        max_lost_time=item.max_lost_time,
        cov_time=item.cov_time)
        new.save()
    return HttpResponse('数据添加成功')
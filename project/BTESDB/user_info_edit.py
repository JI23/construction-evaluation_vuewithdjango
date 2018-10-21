from django.http import JsonResponse
from .models import User_Info
from django.core import serializers
import json

def get_user_info(request):
    print('get_user_info')
    response={}
    try:
        username=request.GET['username']
        this_user=User_Info.objects.get(username=username)
        print(this_user)
        response['user_info']=json.loads(serializers.serialize("json", this_user))
        response['msg']='获取用户资料成功'
        response['error_num']=0
    except Exception as e:
        print (str(e))
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)

def edit_user_info(request):
    print('edit_user_info')
    response={}
    try:
        username=request.GET['username']
        this_user=User_Info.objects.get(username=username)
        print(this_user)
        #没写完
    except Exception as e:
        print (str(e))
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)
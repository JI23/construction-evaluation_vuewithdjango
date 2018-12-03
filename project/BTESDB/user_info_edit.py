from django.http import JsonResponse
from .models import User_Info
from django.core import serializers
import json

def get_user_info(request):
    print('get_user_info')
    response={}
    #user={}
    try:
        username=request.GET['username']
<<<<<<< HEAD
        this_user=User_Info.objects.filter(username=username).values("username","telephone","truename","email","nickname","architect_id","job","company__com_name","company__certificate")
=======
        this_user=User_Info.objects.filter(username=username).values("telephone","truename","email","nickname","architect_id","job","company__com_name","company__certificate")
>>>>>>> upstream/master
        this_user=this_user[0]
        print(this_user)
        '''
        user['telephone']=this_user.telephone
        user['truename']=this_user.truename
        user['email']=this_user.email
        user['nickname']=this_user.nickname
        user['architect_id']=this_user.architect_id
        user['job']=this_user.job
        user['company__com_name']=this_user.company__com_name
        user['company__certificate']=this_user.company__certificate
        '''
        response['user_info']=this_user
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
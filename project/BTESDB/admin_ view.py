



@csrf_exempt
def show_projects_all(request):
    response = {}
    try:
        projects = Project.objects.all() 
        
        response['list']  = json.loads(serializers.serialize("json", projects))
        response['msg'] = 'success'
        response['error_num'] = 0
        #print (response)
    except  Exception as e:
        print (2)
        response['msg'] = str(e)
        response['error_num'] = 1
    print (3)
    return JsonResponse(response)
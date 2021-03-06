from .rate import get_project_dedail,generatePDF
from django.http import JsonResponse
from .models import Project

def preview(request):
    print('preview')
    response={}
    try:
        #获取数据
        project=request.GET['project']
        ProjectInfoDict=dict()
        BuildingInfoDict=dict()
        FloorsList=list()
        StructureElementsList=list()
        NonStructureElementsList=list()
        EarthquakeInfoDict=dict()
        EarthquakeWaveList=list()
        StructureResponseList=list()

        ProjectInfoDict,BuildingInfoDict,FloorsList,StructureElementsList,NonStructureElementsList,EarthquakeInfoDict,EarthquakeWaveList,StructureResponseList = get_project_dedail(project)
        for item in EarthquakeWaveList:
            item['earthquake_wave_file']=str(item['earthquake_wave_file'])
        for item in StructureElementsList:
            item['xml']=str(item['xml'])
        for item in NonStructureElementsList:
            item['xml']=str(item['xml'])
        response['ProjectInfoDict']=ProjectInfoDict
        response['BuildingInfoDict']=BuildingInfoDict
        response['FloorsList']=FloorsList
        response['StructureElementsList']=StructureElementsList
        response['NonStructureElementsList']=NonStructureElementsList
        response['EarthquakeInfoDict']=EarthquakeInfoDict
        response['EarthquakeWaveList']=EarthquakeWaveList
        response['StructureResponseList']=StructureResponseList
        print ('生成PDF')
        result=['尚未定级','尚未定级','尚未定级','尚未定级','尚未定级']
        generatePDF(result,ProjectInfoDict,BuildingInfoDict,FloorsList,StructureElementsList,NonStructureElementsList,EarthquakeInfoDict,EarthquakeWaveList,StructureResponseList)

        this_project=Project.objects.get(id=ProjectInfoDict['id'])
        print('成功')
        print(this_project.PDF)
        response['error_num']=0
        response['PDF']=str(this_project.PDF)
        response['msg']='获取预览信息成功'
    except Exception as e:
        print(str(e))
        response['error_num']=1
        response['msg']='有误'
    return JsonResponse(response)


from .rate import get_project_dedail
from django.http import JsonResponse
import pdfkit
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
        result='尚未定级'
        generatePDF(result,ProjectInfoDict,BuildingInfoDict,FloorsList,StructureElementsList,NonStructureElementsList,EarthquakeInfoDict,EarthquakeWaveList,StructureResponseList)

        print('成功')
        response['error_num']=0
        response['msg']='获取预览信息成功'
    except Exception as e:
        print(str(e))
        response['error_num']=1
        response['msg']='有误'
    return JsonResponse(response)

def generatePDF(result,ProjectInfoDict,BuildingInfoDict,FloorsList,StructureElementsList,NonStructureElementsList,EarthquakeInfoDict,EarthquakeWaveList,StructureResponseList):
    f = open('./media/project/'+str(ProjectInfoDict['id'])+'/project.html','w')
    message = """
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
    <title>定级报告</title>
    </head>
    <body>"""
    message += '<h1 style="text-align:center" >项目名称：' + ProjectInfoDict['project_name']+'</h1>'

    message += '<hr /><h3>项目信息</h3>'
    message += '<h1>项目定级:' +result +'</h1>'
    message += '<p>客户名称:' + ProjectInfoDict['client_name']+'</p>'
    message += '<p>负责人:' + ProjectInfoDict['project_leader']+'</p>'
    message += '<p>项目描述:'+ ProjectInfoDict['project_description']+'</p>'
    message += '<hr />'

    message +='<h3>建筑信息</h3>'
    message +='<p>建筑材料:' +BuildingInfoDict['material'] +'</p>'
    message +='<p>结构类型:' +BuildingInfoDict['structure_type']+'</p>'
    message +='<p>图审时间:' +BuildingInfoDict['figure_time'].strftime('%Y-%m-%d')+'</p>'
    message +='<p>建筑高度:' +str(BuildingInfoDict['height'])+'</p>'
    message +='<p>建筑层数:' +str(BuildingInfoDict['floor'])+'</p>'
    message +='<p>建筑面积:' +str(BuildingInfoDict['area'])+'</p>'
    message +='<p>每平米造价:' +str(BuildingInfoDict['cost_per_squaremeter']) +'</p>'

    message +='<h4>楼层详情</h4>'
    message +='<table border="1">'
    message +="""<tr>
        <th>楼层号</th>
        <th>楼层高度</th>
        <th>楼层面积</th>
        <th>楼层影响系数</th>
        <th>人口密度</th>
        </tr>"""
    for floorDict in FloorsList:
        message +='<tr>'
        message += '<td>'+str(floorDict['floor_no'])+'</td>'
        message += '<td>'+str(floorDict['floor_height'])+'</td>'
        message += '<td>'+str(floorDict['floor_area'])+'</td>'
        message += '<td>'+str(floorDict['influence_coefficient'])+'</td>'
        message += '<td>'+str(floorDict['population_density'])+'</td>'
        message +='</tr>'
    message +='</table>'
    message += '<hr />'

    message +='<h3>结构构件</h3>'
    message +='<table border="1">'
    message +="""<tr>
        <th>易损件ID</th>
        <th>起始楼层</th>
        <th>终止楼层</th>
        <th>X方向个数</th>
        <th>Y方向个数</th>
        <th>无方向个数</th>
        </tr>"""
    for SEDict in StructureElementsList:
        message +='<tr>'
        message += '<td>'+SEDict['part_id']+'</td>'
        message += '<td>'+str(SEDict['start_floor'])+'</td>'
        message += '<td>'+str(SEDict['stop_floor'])+'</td>'
        message += '<td>'+str(SEDict['X'])+'</td>'
        message += '<td>'+str(SEDict['Y'])+'</td>'
        message += '<td>'+str(SEDict['Non'])+'</td>'
        message +='</tr>'
    message += '</table>'
    message += '<hr />'

    message +='<h3>非结构构件</h3>'
    message +='<table border="1">'
    message +="""<tr>
        <th>易损件ID</th>
        <th>起始楼层</th>
        <th>终止楼层</th>
        <th>X方向个数</th>
        <th>Y方向个数</th>
        <th>无方向个数</th>
        </tr>"""
    for NSEDict in NonStructureElementsList:
        message +='<tr>'
        message += '<td>'+NSEDict['part_id']+'</td>'
        message += '<td>'+str(NSEDict['start_floor'])+'</td>'
        message += '<td>'+str(NSEDict['stop_floor'])+'</td>'
        message += '<td>'+str(NSEDict['X'])+'</td>'
        message += '<td>'+str(NSEDict['Y'])+'</td>'
        message += '<td>'+str(NSEDict['Non'])+'</td>'
        message +='</tr>'
    message += '</table>'
    message += '<hr />'

    message +='<h3>地震信息</h3>'
    message += '<p>设防烈度:' + str(EarthquakeInfoDict['defense_intensity'])+'</p>'
    message += '<p>地震波数:' + str(EarthquakeInfoDict['number'])+'</p>'
    message += '<p>峰值加速度:' + str(EarthquakeInfoDict['peak_acceleration'])+'</p>'
    message += '<p>场地类别:' + EarthquakeInfoDict['site_type']+'</p>'
    message += '<p>地震分组:' + str(EarthquakeInfoDict['group'])+'</p>'
    message += '<p>地震水准:' + EarthquakeInfoDict['earthquake_level']+'</p>'
    message +='<h4>地震详情</h4>'
    message +='<table border="1">'
    message +="""<tr>
        <th>地震波编号</th>
        <th>地震波名称</th>
        <th>地震波峰值</th>
        <th>地震波文件</th>
        </tr>"""
    for EarthquakeWaveDict in EarthquakeWaveList:
        message +='<tr>'
        message += '<td>'+str(EarthquakeWaveDict['earthquake_wave_no'])+'</td>'
        message += '<td>'+EarthquakeWaveDict['earthquake_wave_name']+'</td>'
        message += '<td>'+str(EarthquakeWaveDict['peak'])+'</td>'
        message += '<td>'+EarthquakeWaveDict['earthquake_wave_file']+'</td>'
        message +='</tr>'
    message +='</table>'
    message += '<hr />'

    message +='<h3>结构响应</h3>'
    for StructureResponseDict in  StructureResponseList:
        message +='<p>方向：'+StructureResponseDict['direction']
        message +='\t\tEDP类型：'+StructureResponseDict['EDP_type']+'</p>'
        x=int(0)
        message +='<table border="1">'
        message +='<tr><th>楼层</th>'
        for j in range(StructureResponseDict['earthquake_no']):
            message += '<th>地震'+str(j+1)+'</th>'
        message += '</tr>'
        for i in range (StructureResponseDict['floor_no']):
            message += '<tr>'
            message += '<td>楼层'+str(i+1)+'</td>'
            for j in range(StructureResponseDict['earthquake_no']):
                message += '<td>'+StructureResponseDict['data'][x]+'</td>'
                x += 1
            message += '</tr>'
        message += '</table>'
    
    message += "</body></html>"
    f.write(message)
    f.close()
    pdfkit.from_file('./media/project/'+str(ProjectInfoDict['id'])+'/project.html','./media/project/'+str(ProjectInfoDict['id'])+'/project.pdf')
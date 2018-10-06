from .models import *
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict 
import os

def rate(request):
    print(rate)
    response={}
    try:
        #获取数据
        project=request.GET['project']

        ProjectInfo=Project.objects.get(id=project)
        ProjectInfoDict=model_to_dict(ProjectInfo)
        print(ProjectInfoDict)

        Floors=Floor_Info.objects.filter(project=project)
        FloorsList=list()
        for i in Floors:
            floorDict=model_to_dict(i)
            print(floorDict)
            FloorsList.append(floorDict)
        
        StructureElements=Element.objects.filter(project=project,element_type='s')
        StructureElementsList=list()
        for i in StructureElements:
            SEDict=model_to_dict(i)
            element_id=SEDict['element']
            this_DB_part=DB_part.objects.get(id=element_id)
            this_DB_partDict=model_to_dict(this_DB_part)
            this_DB_partDict.pop('id')
            SEDict.update(this_DB_partDict)
            print(SEDict)
            StructureElementsList.append(SEDict)

        NonStructureElements=Element.objects.filter(project=project,element_type='n')
        NonStructureElementsList=list()
        for i in NonStructureElements:
            NSEDict=model_to_dict(i)
            element_id=NSEDict['element']
            this_DB_part=DB_part.objects.get(id=element_id)
            this_DB_partDict=model_to_dict(this_DB_part)
            this_DB_partDict.pop('id')
            NSEDict.update(this_DB_partDict)
            print(NSEDict)
            NonStructureElementsList.append(NSEDict)

        EarthquakeInfo=Earthquake_Info.objects.get(project=project)
        EarthquakeInfoDict=model_to_dict(EarthquakeInfo)
        print(EarthquakeInfoDict)

        EarthquakeWave=Earthquake_wave_detail.objects.filter(project=project)
        EarthquakeWaveList=list()
        for i in EarthquakeWave:
            EarthquakeWaveDict=model_to_dict(i)
            print(EarthquakeWaveDict)
            EarthquakeWaveList.append(EarthquakeWaveDict)

        StructureResponse=Structure_response.objects.filter(project=project)
        StructureResponseList=list()
        for i in StructureResponse:
            StructureResponseDict=model_to_dict(i)
            print(StructureResponseDict)
            StructureResponseList.append(StructureResponseDict)
        
        result=xmlProject(ProjectInfoDict,FloorsList,StructureElementsList,NonStructureElementsList,
        EarthquakeInfoDict,EarthquakeWaveList,StructureResponseList)

        response['error_num']=0
        response['msg']='项目xml文件新建成功!'+'\n 你的定级结果是：'+str(result)
        ProjectInfo.is_finished=True
        ProjectInfo.rate=result
        ProjectInfo.save()
    except Exception as e:
        print(str(e))
        response['error_num']=1
        response['msg']='有误'
    return JsonResponse(response)

import xml.etree.ElementTree as ET
def addFloor(path,floorDict):
    print('addFloor')
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    BuildingInfo=root.find('BuildingInfo')
    Floors=BuildingInfo.find('Floors')

    Floor=ET.SubElement(Floors,'Floor',{'FloorNo':str(floorDict['floor_no'])})
    FloorID=ET.SubElement(Floor,'FloorID');FloorID.text=str(floorDict['floor_no'])
    FloorHeight=ET.SubElement(Floor,'FloorHeight');FloorHeight.text=str(floorDict['floor_height'])
    FloorArea=ET.SubElement(Floor,'FloorArea');FloorArea.text=str(floorDict['floor_area'])
    InfluenceCoefficient=ET.SubElement(Floor,'InfluenceCoefficient');InfluenceCoefficient.text=str(floorDict['influence_coefficient'])
    PopulationDensity=ET.SubElement(Floor,'PopulationDensity');PopulationDensity.text=str(floorDict['population_density'])

    tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")

def addStructuralElement(path,sNo,SEDict):
    print('addStructuralElement')
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    StructuralElements=root.find('StructuralElements')

    StructuralElement=ET.SubElement(StructuralElements,'StructuralElement',{'StructuralElementNo':str(sNo)})
    ElementID=ET.SubElement(StructuralElement,'ElementID');ElementID.text=SEDict['part_id']
    StartFloor=ET.SubElement(StructuralElement,'StartFloor');StartFloor.text=str(SEDict['start_floor'])
    StopFloor=ET.SubElement(StructuralElement,'StopFloor');StopFloor.text=str(SEDict['stop_floor'])
    XNumber=ET.SubElement(StructuralElement,'XNumber');XNumber.text=str(SEDict['X'])
    YNumber=ET.SubElement(StructuralElement,'YNumber');YNumber.text=str(SEDict['Y'])
    NonNumber=ET.SubElement(StructuralElement,'NonNumber');NonNumber.text=str(SEDict['Non'])

    xml_path=DB_part.objects.get(part_id=SEDict['part_id']).xml.path
    #print(SEDict)
    print(xml_path)
    tree1=ET.ElementTree(file=xml_path)
    root1=tree1.getroot()

    Cost=ET.SubElement(ElementID,'Cost')
    Cost1=root1.find('Cost')
    Cost.text='1'#Cost1.text
    EDP_kind=ET.SubElement(ElementID,'EDP_kind')
    EDPType=root1.find('EDPType')
    EDP_kind1=EDPType.find('TypeName')
    EDP_kind.text=EDP_kind1.text
    UseEDPValueOfFloorAbove=ET.SubElement(ElementID,'UseEDPValueOfFloorAbove')
    UseEDPValueOfFloorAbove1=root1.find('UseEDPValueOfFloorAbove')
    UseEDPValueOfFloorAbove.text=UseEDPValueOfFloorAbove1.text
    RepairWorkNumber=ET.SubElement(ElementID,'RepairWorkNumber')
    #RepairWorkNumber1=root1.find('Directional')
    RepairWorkNumber.text='3'
    DSNum=ET.SubElement(ElementID,'DSNum')
    DamageStates1=root1.find('DamageStates')
    DSNum1=DamageStates1.findall('DamageState')
    DSNum.text=str(len(DSNum1))
    Direction=ET.SubElement(ElementID,'Direction')
    Direction1=root1.find('Directional')
    Direction.text=Direction1.text
    DamageStates=ET.SubElement(ElementID,'DamageStates')
    for item in DSNum1:
        print(item)
        DamageState=ET.SubElement(DamageStates,'DamageState')
        Cost_LowerQuantity=ET.SubElement(DamageState,'Cost_LowerQuantity')
        Cost_MaxAmount=ET.SubElement(DamageState,'Cost_MaxAmount')
        Cost_UpperQuantity=ET.SubElement(DamageState,'Cost_UpperQuantity')
        Cost_MinAmount=ET.SubElement(DamageState,'Cost_MinAmount')
        Time_LowerQuantity=ET.SubElement(DamageState,'Time_LowerQuantity')
        Time_MaxAmount=ET.SubElement(DamageState,'Time_MaxAmount')
        Time_UpperQuantity=ET.SubElement(DamageState,'Time_UpperQuantity')
        Time_MinAmount=ET.SubElement(DamageState,'Time_MinAmount')
        Median=ET.SubElement(DamageState,'Median')
        Beta=ET.SubElement(DamageState,'Beta')
        DSNum.text=str(len(DSNum1))
        ConsequenceGroup1=item.find('ConsequenceGroup')
        CostConsequence1=ConsequenceGroup1.find('CostConsequence')
        Cost_LowerQuantity1=CostConsequence1.find('LowerQuantity')
        Cost_LowerQuantity.text=Cost_LowerQuantity1.text
        Cost_MaxAmount1=CostConsequence1.find('MaxAmount')
        Cost_MaxAmount.text=Cost_MaxAmount1.text
        Cost_UpperQuantity1=CostConsequence1.find('UpperQuantity')
        Cost_UpperQuantity.text=Cost_UpperQuantity1.text
        Cost_MinAmount1=CostConsequence1.find('MinAmount')
        Cost_MinAmount.text=Cost_MinAmount1.text
        TimeConsequence1=ConsequenceGroup1.find('TimeConsequence')
        Time_LowerQuantity1=TimeConsequence1.find('LowerQuantity')
        Time_LowerQuantity.text=Time_LowerQuantity1.text
        Time_MaxAmount1=TimeConsequence1.find('MaxAmount')
        Time_MaxAmount.text=Time_MaxAmount1.text
        Time_UpperQuantity1=TimeConsequence1.find('UpperQuantity')
        Time_UpperQuantity.text=Time_UpperQuantity1.text
        Time_MinAmount1=TimeConsequence1.find('MinAmount')
        Time_MinAmount.text=Time_MinAmount1.text
        Median1=item.find('Median')
        Median.text=Median1.text
        Beta1=item.find('Beta')
        Beta.text=Beta1.text


    tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")

def addNonStructuralElement(path,nsNo,NSEDict):
    print('addNonStructuralElement')
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    NonStructuralElements=root.find('NonStructuralElements')

    NonStructuralElement=ET.SubElement(NonStructuralElements,'NonStructuralElement',{'NonStructuralElementNo':str(nsNo)})
    ElementID=ET.SubElement(NonStructuralElement,'ElementID');ElementID.text=NSEDict['part_id']
    StartFloor=ET.SubElement(NonStructuralElement,'StartFloor');StartFloor.text=str(NSEDict['start_floor'])
    StopFloor=ET.SubElement(NonStructuralElement,'StopFloor');StopFloor.text=str(NSEDict['stop_floor'])
    XNumber=ET.SubElement(NonStructuralElement,'XNumber');XNumber.text=str(NSEDict['X'])
    YNumber=ET.SubElement(NonStructuralElement,'YNumber');YNumber.text=str(NSEDict['Y'])
    NonNumber=ET.SubElement(NonStructuralElement,'NonNumber') ;NonNumber.text=str(NSEDict['Non'])

    xml_path=DB_part.objects.get(part_id=NSEDict['part_id']).xml.path
    
    tree1=ET.ElementTree(file=xml_path)
    root1=tree1.getroot()

    Cost=ET.SubElement(ElementID,'Cost')
    Cost1=root1.find('Cost')
    Cost.text=Cost1.text
    EDP_kind=ET.SubElement(ElementID,'EDP_kind')
    EDPType=root1.find('EDPType')
    EDP_kind1=EDPType.find('TypeName')
    EDP_kind.text=EDP_kind1.text
    UseEDPValueOfFloorAbove=ET.SubElement(ElementID,'UseEDPValueOfFloorAbove')
    UseEDPValueOfFloorAbove1=root1.find('UseEDPValueOfFloorAbove')
    UseEDPValueOfFloorAbove.text=UseEDPValueOfFloorAbove1.text
    RepairWorkNumber=ET.SubElement(ElementID,'RepairWorkNumber')
    RepairWorkNumber1=root1.find('RepairWorkNumber')
    RepairWorkNumber.text=RepairWorkNumber1.text
    DSNum=ET.SubElement(ElementID,'DSNum')
    DamageStates1=root1.find('DamageStates')
    DSNum1=DamageStates1.findall('DamageState')
    DSNum.text=str(len(DSNum1))
    Direction=ET.SubElement(ElementID,'Direction')
    Direction1=root1.find('Directional')
    Direction.text=Direction1.text
    DamageStates=ET.SubElement(ElementID,'DamageStates')
    for item in DSNum1:
        print(item)
        DamageState=ET.SubElement(DamageStates,'DamageState')
        Cost_LowerQuantity=ET.SubElement(DamageState,'Cost_LowerQuantity')
        Cost_MaxAmount=ET.SubElement(DamageState,'Cost_MaxAmount')
        Cost_UpperQuantity=ET.SubElement(DamageState,'Cost_UpperQuantity')
        Cost_MinAmount=ET.SubElement(DamageState,'Cost_MinAmount')
        Time_LowerQuantity=ET.SubElement(DamageState,'Time_LowerQuantity')
        Time_MaxAmount=ET.SubElement(DamageState,'Time_MaxAmount')
        Time_UpperQuantity=ET.SubElement(DamageState,'Time_UpperQuantity')
        Time_MinAmount=ET.SubElement(DamageState,'Time_MinAmount')
        Median=ET.SubElement(DamageState,'Median')
        Beta=ET.SubElement(DamageState,'Beta')
        DSNum.text=str(len(DSNum1))
        ConsequenceGroup1=item.find('ConsequenceGroup')
        CostConsequence1=ConsequenceGroup1.find('CostConsequence')
        Cost_LowerQuantity1=CostConsequence1.find('LowerQuantity')
        Cost_LowerQuantity.text=Cost_LowerQuantity1.text
        Cost_MaxAmount1=CostConsequence1.find('MaxAmount')
        Cost_MaxAmount.text=Cost_MaxAmount1.text
        Cost_UpperQuantity1=CostConsequence1.find('UpperQuantity')
        Cost_UpperQuantity.text=Cost_UpperQuantity1.text
        Cost_MinAmount1=CostConsequence1.find('MinAmount')
        Cost_MinAmount.text=Cost_MinAmount1.text
        TimeConsequence1=ConsequenceGroup1.find('TimeConsequence')
        Time_LowerQuantity1=TimeConsequence1.find('LowerQuantity')
        Time_LowerQuantity.text=Time_LowerQuantity1.text
        Time_MaxAmount1=TimeConsequence1.find('MaxAmount')
        Time_MaxAmount.text=Time_MaxAmount1.text
        Time_UpperQuantity1=TimeConsequence1.find('UpperQuantity')
        Time_UpperQuantity.text=Time_UpperQuantity1.text
        Time_MinAmount1=TimeConsequence1.find('MinAmount')
        Time_MinAmount.text=Time_MinAmount1.text
        Median1=item.find('Median')
        Median.text=Median1.text
        Beta1=item.find('Beta')
        Beta.text=Beta1.text

    tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")


def addEarthquakeWave(path,EarthquakeWaveDict):
    print('addEarthquakeWave')
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    Earthquake_Info=root.find('EarthquakeInfo')
    EarthquakeWaves=Earthquake_Info.find('EarthquakeWaves')    
    EarthquakeWave=ET.SubElement(EarthquakeWaves,'EarthquakeWave',{'waveNo':str(EarthquakeWaveDict['earthquake_wave_no'])})
    WaveID=ET.SubElement(EarthquakeWave,'WaveID');WaveID.text=str(EarthquakeWaveDict['earthquake_wave_no'])
    WaveName=ET.SubElement(EarthquakeWave,'WaveName');WaveName.text=EarthquakeWaveDict['earthquake_wave_name']
    WavePeak=ET.SubElement(EarthquakeWave,'WavePeak');WavePeak.text=str(EarthquakeWaveDict['peak'])  
    WaveFile=ET.SubElement(EarthquakeWave,'WaveFile');WaveFile.text=str(EarthquakeWaveDict['earthquake_wave_file'])
    
    tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")


def Judge(StructureResponseDict):
    target=str()
    if StructureResponseDict['direction']=='X':
        target="X-"
    else:
        target="Y-"
    if StructureResponseDict['EDP_type']=='S':
        target += "SDR"
    else:
        target += "ACC"
    return target

def addStructureResponse(path,StructureResponseDict):
    print('addStructureResponse')
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    StructureResponse=root.find("StructureResponse")
    target=Judge(StructureResponseDict)
    place=StructureResponse.find(target)
    #开始赋值
    x=int(0)
    for i in range (StructureResponseDict['floor_no']):
        Floor=ET.SubElement(place,"Floor",{'FloorNo':str(i+1)})
        for j in range(StructureResponseDict['earthquake_no']):
            Earthquake=ET.SubElement(Floor,'Earthquake',{'EarthquakeNo':str(j+1)})
            double=ET.SubElement(Earthquake,"double");double.text=StructureResponseDict['data'][x]
            x += 1
    tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")



from datetime import datetime
def xmlProject(ProjectInfoDict,FloorsList,StructureElementsList,NonStructureElementsList,
        EarthquakeInfoDict,EarthquakeWaveList,StructureResponseList):
    print('xmlProject')
    print(ProjectInfoDict)
    print(type(ProjectInfoDict))
    root=ET.Element('Project',{'ProjectID':'"1.0"'})
    
    #项目信息
    ProjectInfo=ET.SubElement(root,'ProjectInfo')
    ProjectName=ET.SubElement(ProjectInfo,'ProjectName');ProjectName.text=ProjectInfoDict['project_name']
    ClientName=ET.SubElement(ProjectInfo,'ClientName');ClientName.text=ProjectInfoDict['client_name']
    ProjectLeader=ET.SubElement(ProjectInfo,'ProjectLeader');ProjectLeader.text=ProjectInfoDict['project_leader']
    ProjectDescription=ET.SubElement(ProjectInfo,'ProjectDescription');ProjectDescription.text=ProjectInfoDict['project_description']
    
    #建筑信息
    BuildingInfo=ET.SubElement(root,'BuildingInfo')
    BuildingMaterial=ET.SubElement(BuildingInfo,'BuildingMaterial');BuildingMaterial.text=ProjectInfoDict['material']
    FigureTime=ET.SubElement(BuildingInfo,'FigureTime');FigureTime.text=ProjectInfoDict['figure_time'].strftime('%Y-%m-%d')
    StructureHeight=ET.SubElement(BuildingInfo,'StructureHeight');StructureHeight.text=str(ProjectInfoDict['height'])
    StructureType=ET.SubElement(BuildingInfo,'StructureType');StructureType.text=ProjectInfoDict['structure_type']
    StructureFloorsNumber=ET.SubElement(BuildingInfo,'StructureFloorsNumber');StructureFloorsNumber.text=str(ProjectInfoDict['floor'])
    BuildingArea=ET.SubElement(BuildingInfo,'BuildingArea');BuildingArea.text=str(ProjectInfoDict['area'])
    UnitCost=ET.SubElement(BuildingInfo,'UnitCost');UnitCost.text=str(ProjectInfoDict['cost_per_squaremeter'])
    Floors=ET.SubElement(BuildingInfo,'Floors')

    #结构构件
    StructuralElements=ET.SubElement(root,'StructuralElements')

    #非结构构件
    NonStructuralElements=ET.SubElement(root,'NonStructuralElements')

    #地震信息
    EarthquakeInfo=ET.SubElement(root,'EarthquakeInfo')
    DefenseIntensity=ET.SubElement(EarthquakeInfo,'DefenseIntensity');DefenseIntensity.text=str(EarthquakeInfoDict['defense_intensity'])
    EarthquakeWaveNumber=ET.SubElement(EarthquakeInfo,'EarthquakeWaveNumber');EarthquakeWaveNumber.text=str(EarthquakeInfoDict['number'])
    PeakAcceleration=ET.SubElement(EarthquakeInfo,'PeakAcceleration');PeakAcceleration.text=str(EarthquakeInfoDict['peak_acceleration'])
    SiteType=ET.SubElement(EarthquakeInfo,'SiteType');SiteType.text=EarthquakeInfoDict['site_type']
    EarthquakeGroup=ET.SubElement(EarthquakeInfo,'EarthquakeGroup');EarthquakeGroup.text=str(EarthquakeInfoDict['group'])
    EarthquakeLevel=ET.SubElement(EarthquakeInfo,'EarthquakeLevel');EarthquakeLevel.text=EarthquakeInfoDict['earthquake_level']
    EarthquakeWaves=ET.SubElement(EarthquakeInfo,'EarthquakeWaves')
    #EarthquakeWave=ET.SubElement(EarthquakeWaves,'EarthquakeWave',{'waveNo':str(1)})
   
    #结构响应
    StructureResponse=ET.SubElement(root,'StructureResponse')
    FloorsNumber=ET.SubElement(StructureResponse,'FloorsNumber');FloorsNumber.text=str(ProjectInfoDict['floor'])
    EarthquakeNumber=ET.SubElement(StructureResponse,'EarthquakeNumber');EarthquakeNumber.text=str(EarthquakeInfoDict['number'])
    X_SDR=ET.SubElement(StructureResponse,'X-SDR')
    X_ACC=ET.SubElement(StructureResponse,'X-ACC')
    Y_SDR=ET.SubElement(StructureResponse,'Y-SDR')
    Y_ACC=ET.SubElement(StructureResponse,'Y-ACC')
    
    Tree=ET.ElementTree(root)
    print(type(Tree))
    path='./media/project/'+str(ProjectInfoDict['id'])+'/project.xml'
    d='./media/project/'+str(ProjectInfoDict['id'])
    folder = os.path.exists(d)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
	    os.makedirs(d)            #makedirs 创建文件时如果路径不存在会创建这个路径
	    print ('创建文件夹成功')
    Tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")
    
    #新增楼层
    for floorDict in FloorsList:
        addFloor(path,floorDict)
    
    #新增结构构件
    sNo=int(1)
    for SEDict in StructureElementsList:
        addStructuralElement(path,sNo,SEDict)
        sNo += 1
    
    #新增非结构构件
    nsNo=int(1)
    for NSEDict in NonStructureElementsList:
        addNonStructuralElement(path,nsNo,NSEDict)
        nsNo += 1
    
    #新增地震波
    for EarthquakeWaveDict in EarthquakeWaveList:
        addEarthquakeWave(path,EarthquakeWaveDict)

    #新增结构响应
    for StructureElementsDict in  StructureResponseList:
        data=StructureElementsDict['data']
        StructureElementsDict['data']=data[1:-1].split(", ")
        addStructureResponse(path,StructureElementsDict)
    result = runDll(path)
    return result

from ctypes import *
from reportlab.pdfgen import canvas
def runDll(project_file_path):
    print("runDll")
    print(project_file_path)
    dll =cdll.LoadLibrary("./x64//Release//Dll3.dll")
    #readfile=dll.pl
    #readfile.argtypes=[c_char_p]
    #readfile.restype=c_int
    s=(c_char * 100)(*bytes(project_file_path,"utf-8"))
    CostStar=dll.TryGetCostStar
    CostStar.argtypes=[c_char_p]
    CostStar.restype=c_int
    h1=CostStar(s)
    h1="CostStar:"+str(h1)

    TimeStar=dll.TryGetTimeStar
    TimeStar.argtypes=[c_char_p]
    TimeStar.restype=c_int
    h2=TimeStar(s)
    h2="TimeStar:"+str(h2)

    CalsualtyStar=dll.TryGetCalsualtyStar
    CalsualtyStar.argtypes=[c_char_p]
    CalsualtyStar.restype=c_int
    h3=CalsualtyStar(s)
    h3="CalsualtyStar:"+str(h3)

    FinalStar=dll.TryGetFinalStar
    FinalStar.argtypes=[c_char_p]
    FinalStar.restype=c_int
    h4=FinalStar(s)
    h5="FinalStar:"+str(h4)

    print("s success")
    #h=readfile(s)
    #print(h)
    pdf_path=project_file_path.replace("xml","pdf")
    print(pdf_path)
    h6=h1+'   '+h2+'    '+h3+'   '+h5
    c=canvas.Canvas(pdf_path)
    c.drawString(100,700,str(h6))
    #c.drawString(100,100,"rating result")
    c.showPage()
    c.save()
    return h4
    

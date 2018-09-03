from .models import *
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict 
def rate(request):
    print(rate)
    response={}
    try:
        #获取数据
        project=request.GET['project']
        ProjectInfo= Project.objects.get(id=project)
        pd=model_to_dict(ProjectInfo)
        print(pd)
        print(type(pd))

        Floors=Floor_Info.objects.filter(project=project)
        print(Floors)
        print(type(Floors))
        for i in Floors:
            fd=model_to_dict(i)
            print(fd)
        StructureElements=Element.objects.filter(project=project,element_type='s')
        NonStructureElements=Element.objects.filter(project=project,element_type='n')
        EarthquakeInfo=Earthquake_Info.objects.filter(project=project)
        EarthquakeWave=Earthquake_wave_detail.objects.filter(project=project)
        StructureResponse=Earthquake_wave_detail.objects.filter(project=project)
        xmlProject(pd,Floors,StructureElements,NonStructureElements,
        EarthquakeInfo,EarthquakeWave,StructureResponse)
        response['error_num']=0
        response['msg']='项目xml文件新建成功'
    except Exception as e:
        print(str(e))
        response['error_num']=1
        response['msg']='有误'
    return JsonResponse(response)

import xml.etree.ElementTree as ET
def addFloor(path,floorNo):
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    BuildingInfo=root.find('BuildingInfo')
    Floors=BuildingInfo.find('Floors')

    Floor=ET.SubElement(Floors,'Floor',{'FloorNo':str(floorNo)})
    FloorID=ET.SubElement(Floor,'FloorID');FloorID.text=''
    FloorHeight=ET.SubElement(Floor,'FloorHeight');FloorHeight.text=''
    FloorArea=ET.SubElement(Floor,'FloorArea');FloorArea.text=''
    InfluenceCoefficient=ET.SubElement(Floor,'InfluenceCoefficient');InfluenceCoefficient.text=''
    PopulationDensity=ET.SubElement(Floor,'PopulationDensity');PopulationDensity.text=''

    tree.write('project.xml',xml_declaration=True, encoding='utf-8', method="xml")

def addStructuralElement(path,sNo):
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    StructuralElements=root.find('StructuralElements')

    StructuralElement=ET.SubElement(StructuralElements,'StructuralElement',{'StructuralElementNo':str(sNo)})
    ElementID=ET.SubElement(StructuralElement,'ElementID');ElementID.text=''
    StartFloor=ET.SubElement(StructuralElement,'StartFloor');StartFloor.text=''
    StopFloor=ET.SubElement(StructuralElement,'StopFloor');StopFloor.text=''
    XNumber=ET.SubElement(StructuralElement,'XNumber');XNumber.text=''
    YNumber=ET.SubElement(StructuralElement,'YNumber');YNumber.text=''
    NonNumber=ET.SubElement(StructuralElement,'NonNumber');NonNumber.text=''

    tree.write('project.xml',xml_declaration=True, encoding='utf-8', method="xml")

def addNonStructuralElement(path,nsNo):
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    NonStructuralElements=root.find('NonStructuralElements')

    NonStructuralElement=ET.SubElement(NonStructuralElements,'NonStructuralElement',{'NonStructuralElementNo':str(nsNo)})
    ElementID=ET.SubElement(NonStructuralElement,'ElementID');ElementID.text=''
    StartFloor=ET.SubElement(NonStructuralElement,'StartFloor');StartFloor.text=''
    StopFloor=ET.SubElement(NonStructuralElement,'StopFloor');StopFloor.text=''
    XNumber=ET.SubElement(NonStructuralElement,'XNumber');XNumber.text=''
    YNumber=ET.SubElement(NonStructuralElement,'YNumber');YNumber.text=''
    NonNumber=ET.SubElement(NonStructuralElement,'NonNumber') ;NonNumber.text=''

    tree.write('project.xml',xml_declaration=True, encoding='utf-8', method="xml")
def addEarthquakeWave(path,waveNo):
    tree=ET.ElementTree(file=path)
    root=tree.getroot()
    Earthquake_Info=root.find('EarthquakeInfo')
    EarthquakeWaves=Earthquake_Info.find('EarthquakeWaves')

    EarthquakeWave=ET.SubElement(EarthquakeWaves,'EarthquakeWave',{'waveNo':str(waveNo)})
    WaveID=ET.SubElement(EarthquakeWave,'WaveID');WaveID.text=''
    WaveName=ET.SubElement(EarthquakeWave,'WaveName');WaveName.text=''
    WavePeak=ET.SubElement(EarthquakeWave,'WavePeak');WavePeak.text=''
    WaveFile=ET.SubElement(EarthquakeWave,'WaveFile');WaveFile.text=''

    tree.write('project.xml',xml_declaration=True, encoding='utf-8', method="xml")
from datetime import datetime
def xmlProject(Project,Floor_Info,Structure,NonStructure,Earthquake_Info,Earthquake_Wave,Structure_Response):
    print('xmlProject')
    print(Project)
    print(type(Project))
    root=ET.Element('Project',{'ProjectID':'"1.0"'})
    
    #项目信息
    ProjectInfo=ET.SubElement(root,'ProjectInfo')
    ProjectName=ET.SubElement(ProjectInfo,'ProjectName');ProjectName.text=Project['project_name']
    ClientName=ET.SubElement(ProjectInfo,'ClientName');ClientName.text=Project['client_name']
    ProjectLeader=ET.SubElement(ProjectInfo,'ProjectLeader');ProjectLeader.text=Project['project_leader']
    ProjectDescription=ET.SubElement(ProjectInfo,'ProjectDescription');ProjectDescription.text=Project['project_description']

    #建筑信息
    BuildingInfo=ET.SubElement(root,'BuildingInfo')
    BuildingMaterial=ET.SubElement(BuildingInfo,'BuildingMaterial');BuildingMaterial.text=Project['material']
    FigureTime=ET.SubElement(BuildingInfo,'FigureTime');FigureTime.text=Project['figure_time'].strftime('%Y-%m-%d')
    StructureHeight=ET.SubElement(BuildingInfo,'StructureHeight');StructureHeight.text=str(Project['height'])
    StructureType=ET.SubElement(BuildingInfo,'StructureType');StructureType.text=Project['structure_type']
    StructureFloorsNumber=ET.SubElement(BuildingInfo,'StructureFloorsNumber');StructureFloorsNumber.text=str(Project['floor'])
    BuildingArea=ET.SubElement(BuildingInfo,'BuildingArea');BuildingArea.text=str(Project['area'])
    UnitCost=ET.SubElement(BuildingInfo,'UnitCost');UnitCost.text=str(Project['cost_per_squaremeter'])
    Floors=ET.SubElement(BuildingInfo,'Floors');Floors.text=''

    #结构构件
    StructuralElements=ET.SubElement(root,'StructuralElements')

    #非结构构件
    NonStructuralElements=ET.SubElement(root,'NonStructuralElements')

    #地震信息
    EarthquakeInfo=ET.SubElement(root,'EarthquakeInfo')
    DefenseIntensity=ET.SubElement(EarthquakeInfo,'DefenseIntensity');DefenseIntensity.text=''
    EarthquakeWaveNumber=ET.SubElement(EarthquakeInfo,'EarthquakeWaveNumber');EarthquakeWaveNumber.text=''
    PeakAcceleration=ET.SubElement(EarthquakeInfo,'PeakAcceleration');PeakAcceleration.text=''
    SiteType=ET.SubElement(EarthquakeInfo,'SiteType');SiteType.text=''
    EarthquakeGroup=ET.SubElement(EarthquakeInfo,'EarthquakeGroup');EarthquakeGroup.text=''
    EarthquakeLevel=ET.SubElement(EarthquakeInfo,'EarthquakeLevel');EarthquakeLevel.text=''
    EarthquakeWaves=ET.SubElement(EarthquakeInfo,'EarthquakeWaves')
   
    #结构响应
    StructureResponse=ET.SubElement(root,'StructureResponse')
    X=ET.SubElement(StructureResponse ,'X')
    EDPType=ET.SubElement(X,'EDPType');EDPType.text=''
    FloorsNumber=ET.SubElement(X,'FloorsNumber');FloorsNumber.text=''
    EarthquakeNumber=ET.SubElement(X,'EarthquakeNumber');EarthquakeNumber.text=''
    Y=ET.SubElement(StructureResponse ,'Y')
    EDPType=ET.SubElement(Y,'EDPType');EDPType.text=''
    FloorsNumber=ET.SubElement(Y,'FloorsNumber');FloorsNumber.text=''
    EarthquakesNumber=ET.SubElement(Y,'EarthquakesNumber');EarthquakesNumber.text=''
    
 

    Tree=ET.ElementTree(root)
    print(type(Tree))
    path='newproject.xml'
    Tree.write(path,xml_declaration=True, encoding='utf-8', method="xml")

    #xmlProject()
    
    #新增楼层
    addFloor(path,1)
        #新增结构构件
    addStructuralElement(path,1)
        #新增非结构构件
    addNonStructuralElement(path,1)
        #新增地震波
    addEarthquakeWave(path,1)

        
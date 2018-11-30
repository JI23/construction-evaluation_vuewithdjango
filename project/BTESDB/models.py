from django.db import models

# Create your models here.
#数据库名Building Toughness Evaluation System Database
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class Company_Info(models.Model):
    '''公司信息表'''
    #com_id=models.AutoField(primary_key=True)#自增长主键
    #公司名
    com_name=models.CharField(max_length=60,blank=False,verbose_name='公司名')
    #18位公司税号
    certificate=models.CharField(max_length=18,unique=True,verbose_name='税号')
    #公司总计多少人使用
    total_user=models.SmallIntegerField(default=0,verbose_name='使用总人数')
    com_tel=models.CharField(max_length=13,verbose_name='电话')#暂定 区号-电话号
    fax=models.CharField(max_length=13,verbose_name='传真')#暂定 区号-电话号
    address=models.CharField(max_length=100,verbose_name='地址')
    def __str__(self):
        return self.com_name
    class Meta:
        verbose_name='公司'
        verbose_name_plural = "公司表"

class User_Info(AbstractUser):
    '''自定义用户信息表，注册时填，登陆时验证'''
    #user_id=models.AutoField(primary_key=True)#自增长主键

    #用户需要填的基本信息
    #指向Company的外键，一个company对应多个user
    company=models.ForeignKey(Company_Info,on_delete=models.CASCADE,default=None,verbose_name='公司')
    
    #昵称，可修改
    nickname=models.CharField(max_length=20,blank=False,editable=True,verbose_name='昵称')
    #用户真实姓名
    truename=models.CharField(max_length=20,blank=False,verbose_name='真实姓名')
    #telephone也是登陆账号 即username
    telephone=models.CharField(max_length=11,unique=True,verbose_name='手机号')
    #建筑师证号，非必填
    architect_id=models.CharField(max_length=12,unique=True,blank=True,verbose_name='建筑师证号')
    #公司职务，非必填
    job=models.CharField(max_length=20,blank=True,verbose_name='公司职务')
    #登陆跟踪信息
    #用户登陆的总次数
    login_amount=models.IntegerField(default=1,verbose_name='登陆次数')
    project_amount=models.SmallIntegerField(default=0,verbose_name='项目数')
    def __str__(self):
        return self.username
    class Meta:
        verbose_name='用户'
        verbose_name_plural = "用户"

    #User模板中已有
    #is_superuser,
    #first_name,last_name
    #password=models.CharField(max_length=80,blank=False)
    #email=models.EmailField(max_length=254,blank=False)
    #last_login=models.DateTimeField()#最后一次成功登陆的时间
    #date_joined=models.DateField(auto_now_add=True)#在第一次创建对象时，设置为当前时间，表注册时间
    #is_active=models.BooleanField(Default=False) #默认为False，表示未通过验证，管理员通过验证后将其改为True


class User_comment(models.Model):
    '''用户评论表（管理员可见）'''
    #django会自己产生一个自增长的主键
    #指向User的外键，一个user对应多个comment
    user=models.ForeignKey(User_Info,on_delete=models.CASCADE)
    comment_id=models.IntegerField()#在同一个user_id内自增长
    class Meta:
        unique_together=("user","comment_id")
        verbose_name='用户评价'
        verbose_name_plural = "用户评价"
    title=models.CharField(max_length=45,verbose_name='标题')#评论标题
    context=models.CharField(max_length=450,blank=False,verbose_name='正文')#评论正文
    response=models.CharField(max_length=450,verbose_name='管理员回复')#管理员回复
    is_response=models.BooleanField(default=False,verbose_name='是否已回复')#标记评论是否被回复
    comment_time=models.DateTimeField(auto_now_add=True,verbose_name='评论时间')#用户评论的时间
    response_time=models.DateTimeField(verbose_name='回复时间')#评论被回复的时间
    def __str__(self):
        return self.comment_id

from django.conf.urls.static import static
from django.conf import settings

def upload_to(instance,filename):
    return '/'.join([instance.get_part_type_display(),instance.part_id,filename])

class DB_part(models.Model):
    '''易损件数据库'''
    #主键由django自行生成
    #指向User的外键，一个user对应多个自定义易损件,对系统给的易损件，user指向一个特定的superuser
    user=models.ForeignKey(User_Info,on_delete=models.CASCADE,verbose_name='用户',default=None)
    #是否是用户自定义
    user_defined=models.BooleanField(default=False,verbose_name='用户自定义')
    #如BE.F.01.01，必须遵循该格式
    part_id=models.CharField(max_length=20,blank=False,verbose_name='易损件id')
    #first & second
    first=models.CharField(max_length=50,verbose_name='第一层分类信息')
    second=models.CharField(max_length=50,verbose_name='第二层分类信息')
    #可以是任意字符串
    part_name=models.CharField(max_length=400,blank=False,verbose_name='易损件名称')
    #如单片玻璃幕墙...
    description=models.CharField(max_length=570,blank=False,verbose_name='易损件描述')
    #基本单位，如1个，3.3m2等
    basic_unit=models.CharField(max_length=10,default='1个',verbose_name='基本单位')
    #易损件单价
    cost=models.DecimalField(max_digits=8, decimal_places=2,blank=False,verbose_name='易损件单价',default=0.00)
    #数据来源
    data_resource=models.CharField(max_length=45,blank=False,default='《建筑抗震韧性评价标准》编委会',verbose_name='数据来源')
    #是否是官方认证
    is_formal=models.BooleanField(default=True,verbose_name='官方认证')
    #易损件的场地类别
    site_classification_choice=(
        ('h','hospital'),
        ('o','office'),
        ('s','school'),
        ('c','common'),
        ('u','user_defined'),
        ('f','FEMA')
    )
    part_type=models.CharField(max_length=1,choices=site_classification_choice,default='c',verbose_name='场地类别')
    #创建时间
    create_date=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    #DSGroupType
    #DSGroupType=models.CharField(max_length=25,verbose_name='DSGroupType')
    #损伤数量
    damage_state_number=models.SmallIntegerField(default=0,verbose_name='损伤数量')
    #与该易损件相关的损伤xml文件
    xml=models.FileField(upload_to=upload_to,blank=True,default=None,verbose_name='xml文件')
    
    #EDP
    #EDP类型，分层间位移角和楼层加速度
    EDP_type_choice=(
        ('S','Story Drift Ratio'),#层间位移角
        ('A','Acceleration'),#楼层加速度
    )
    EDP_type=models.CharField(max_length=1,choices=EDP_type_choice,default='S',verbose_name='EDP类型')
    '''
    #correlation
    correlation=models.BooleanField(default=True,verbose_name='Correlation')
    #directional
    directional=models.BooleanField(default=True,verbose_name='Directional')
    #默认单位
    default_units=models.CharField(max_length=25,verbose_name='默认单位')
    #Dimension
    dimension=models.CharField(max_length=5,verbose_name='Dimension')
    
    
    #Rating
    #DataQuality
    DataQuality=models.CharField(max_length=1,default='1',verbose_name='DataQuality')
    #DataRelevance
    DataRelevance=models.CharField(max_length=1,default='1',verbose_name='DataRelevance')
    #Documentation
    Documentation=models.CharField(max_length=1,default='1',verbose_name='Documentation')
    #Rationality
    Rationality=models.CharField(max_length=1,default='1',verbose_name='Rationality')
    
    
    #Approved
    Approved=models.BooleanField(default=True,verbose_name='Approved')
    #Incomplete
    Incomplete=models.BooleanField(default=True,verbose_name='Incomplete')
    #Notes
    #Notes=models.CharField(max_length=200,blank=True,default=None,verbose_name='Notes')
    #UseEDPValueOfFloorAbove
    UseEDPValueOfFloorAbove=models.BooleanField(default=False,verbose_name='UseEDPValueOfFloorAbove')
    #DSGroupType
    DSGroupType=models.CharField(max_length=25,verbose_name='DSGroupType')
    '''
    class Meta:
        unique_together=('part_id','part_type','user')
        verbose_name='易损件'
        verbose_name_plural='易损件数据库'
    def __str__(self):
        return self.part_id


class Damage_state_detail(models.Model):
    '''易损件损伤详情'''
    #主键由django自行生成
    class Meta:
        verbose_name='易损件损伤'
        verbose_name_plural='易损件损伤详情'
        #unique_together=('DB_part','damage_id')
    DB_part=models.ForeignKey(DB_part,on_delete=models.CASCADE,verbose_name='易损件',default=None)
    #损伤编号，一个自定义易损件对应多个易损件损伤
    damage_id=models.SmallIntegerField(verbose_name='损伤编号')
    #损伤状态
    damage_state=models.CharField(max_length=45,verbose_name='损伤状态',blank=True)
    #损伤状态描述
    damage_description=models.CharField(max_length=300,verbose_name='损伤状态描述')
    #中位值
    median=models.DecimalField(max_digits=5, decimal_places=2,default=0,verbose_name='中位值')
    #方差
    variance=models.DecimalField(max_digits=8, decimal_places=2,default=0,verbose_name='方差')
    #损失参数
    lost_parameter=models.DecimalField(max_digits=5, decimal_places=2,default=0,verbose_name='损失参数')
    #修复系数
    rehabilitation_coeffcient=models.DecimalField(max_digits=5, decimal_places=2,default=0,verbose_name='修复系数')
    #最小工程量折减数量(修复费用)
    min_rehab_cost=models.DecimalField(max_digits=8, decimal_places=2,default=0,verbose_name='最小工程量折减数量(修复费用)')
    #工程量折减系数(修复费用)
    min_lost_cost=models.DecimalField(max_digits=8, decimal_places=2,default=0,verbose_name='工程量折减系数(修复费用)')
    #最大工程量折减数量(修复费用)
    max_rehab_cost=models.DecimalField(max_digits=8, decimal_places=2,default=0,verbose_name='最大工程量折减数量(修复费用)')
    #工程量折减系数(修复费用)
    max_lost_cost=models.DecimalField(max_digits=8, decimal_places=2,default=0,verbose_name='工程量折减系数(修复费用)')
    #费用COV
    cov_cost=models.DecimalField(max_digits=8,decimal_places=4,default=0,verbose_name='费用COV')
    #修复时间(人*天)
    repair_people_day=models.IntegerField(default=0,verbose_name='修复时间(人*天)')
    #最小工程量折减数量(修复时间)
    min_rehab_time=models.DecimalField(max_digits=5, decimal_places=2,default=0,verbose_name='最小工程量折减数量(修复时间)')
    #工程量折减系数(修复时间)
    min_lost_time=models.DecimalField(max_digits=5, decimal_places=2,default=0,verbose_name='工程量折减系数(修复时间)')
    #最大工程量折减数量(修复时间)
    max_rehab_time=models.DecimalField(max_digits=5, decimal_places=2,default=0,verbose_name='最大工程量折减数量(修复时间)')
    #工程量折减系数(修复时间)
    max_lost_time=models.DecimalField(max_digits=5, decimal_places=2,default=0,verbose_name='工程量折减系数(修复时间)')
    #时间COV
    cov_time=models.DecimalField(max_digits=8,decimal_places=4,default=0,verbose_name='时间COV')

class Project(models.Model):
    '''项目信息表'''
    #project_id=models.IntegerField(verbose_name='项目编号')#在同一个user_id内自增长
    user=models.ForeignKey(User_Info,on_delete=models.CASCADE,verbose_name='用户')#指向User的外键，一个user对应多个project
    class Meta:
        #联合主键，但是django会自己产生一个自增长的主键
        unique_together=("user","project_name")
        verbose_name='项目'
        verbose_name_plural='项目'
    #项目名称
    project_name=models.CharField(max_length=45,blank=False,verbose_name='项目名称')
    #客户名称
    client_name=models.CharField(max_length=45,verbose_name='客户名称')
    #项目描述
    project_description=models.CharField(max_length=300,verbose_name='项目描述')
    #项目创建时间
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='项目创建时间')
    #项目负责人
    project_leader=models.CharField(max_length=20,default='unknown',verbose_name='项目负责人')
    #最后一次更新时间
    last_update=models.DateTimeField(auto_now=True,verbose_name='最近更新时间')
    #是否已完成，默认为false
    is_finished=models.BooleanField(default=False,verbose_name='完成')
    #项目定级结果
    rate=models.CharField(max_length=1,verbose_name='最终评级',default='0')
    costrate=models.CharField(max_length=1,verbose_name='修复费用指标评级',default='0')
    timerate=models.CharField(max_length=1,verbose_name='修复时间指标评级',default='0')
    casualtyrate=models.CharField(max_length=1,verbose_name='人员损失评级',default='0')
    #PDF定级报告位置
    PDF=models.CharField(max_length=512,verbose_name='PDF定级报告位置',default='0')

class Building(models.Model):
    #指向Project的外键，一个project对应一个Building
    project=models.ForeignKey(Project,default=None,on_delete=models.CASCADE,verbose_name='项目')    
    #建筑信息
    #材料
    material=models.CharField(max_length=30,blank=False,verbose_name='材料')
    #结构类型
    structure_type=models.CharField(max_length=20,blank=False,verbose_name='结构类型')
    #楼层数
    floor=models.IntegerField(verbose_name='楼层数')
    #图审时间，自己填，须在项目创建时间后
    figure_time=models.DateField(verbose_name='图审时间')
    #楼层总高
    height=models.DecimalField(max_digits=12,decimal_places=6,verbose_name='楼层总高')
    #总面积
    area=models.DecimalField(max_digits=18,decimal_places=6,verbose_name='总面积')
    #每平米造价,非必填
    cost_per_squaremeter=models.DecimalField(max_digits=18,decimal_places=6,verbose_name='每平米造价')
    def __str__(self):
        return str(self.id)

class Floor_Info(models.Model):
    '''楼层信息表'''
    #指向Project的外键，一个project对应多个floor
    project=models.ForeignKey(Project,default=None,on_delete=models.CASCADE,verbose_name='项目')
    #指向User的外键，一个user对应多个floor
    #user=models.ForeignKey(User_Info,on_delete=models.CASCADE,verbose_name='用户')
    #第几层
    floor_no=models.IntegerField(verbose_name='楼层')
    class Meta:
        #联合主键，但是django会自己产生一个自增长的主键 id
        #unique_together=("project","user","floor_no")
        verbose_name='楼层信息'
        verbose_name='楼层信息'
        #楼层高度，范围0-99.99
    floor_height=models.DecimalField(max_digits=10,decimal_places=6,verbose_name='楼层高度')
    #楼层面积，范围0-9999.99
    floor_area=models.DecimalField(max_digits=12,decimal_places=6,verbose_name='楼层面积')
    #楼层影响系，大于1，小于1.5
    influence_coefficient=models.DecimalField(max_digits=7,decimal_places=6,verbose_name='楼层影响系数')
    #人口密度，单位：人/平方米?，待定范围0-9.99
    population_density=models.DecimalField(max_digits=8,decimal_places=6,verbose_name='人口密度')

class Element(models.Model):
    '''构件信息表，包括结构构件和非结构构件'''
    class Meta:
        verbose_name='构建信息'
        verbose_name_plural='构建信息表'
        #联合主键
        #unique_together("project","element_no","element_type")
    #第几个
    #element_no=models.IntegerField(verbose_name='构件编号')
    element_type_choice=(
        ("s","StructuraElement/结构构件"),
        ("n","NonSturctualElement/非结构构件"),
        )
    #是结构构件还是非结构构件
    element_type=models.CharField(max_length=1,choices=element_type_choice,default='s',verbose_name='构建类型')
    #易损件编号，可以是系统带的，也可以是用户自定义的，函数验证合理性
    element=models.ForeignKey(DB_part,default=None,on_delete=models.CASCADE,verbose_name='易损件编号')#如BE.F.01.01
    #指向Project的外键，一个project对应多个构件
    project=models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='项目')
    #验证楼层合理性
    start_floor=models.SmallIntegerField(verbose_name='起始楼层',default=1)
    stop_floor=models.SmallIntegerField(verbose_name='终止楼层',default=1)
    #X,Y,无方向位移数量，可有小数
    X=models.DecimalField(max_digits=12,decimal_places=6,verbose_name='X方向偏移')
    Y=models.DecimalField(max_digits=12,decimal_places=6,verbose_name='Y方向偏移')
    Non=models.DecimalField(max_digits=12,decimal_places=6,verbose_name='无方向偏移')

class Earthquake_Info(models.Model):
    '''地震信息表'''
    #主键由django自己生成
    class Mata:
        verbose_name='地震信息'
        verbose_name_plural='地震信息表'
    #指向Project的外键，一个project对应一个地震信息
    project=models.ForeignKey(Project,default=None,on_delete=models.CASCADE,verbose_name='项目')       
    #设防烈度，由地震水准和场地类别唯一确定
    defense_intensity=models.DecimalField(max_digits=2,decimal_places=1,verbose_name='设防烈度')
    #场地类别
    site_classification_choice=(
        (1,'Ⅰ_0'),
        (2,'Ⅰ_1'),
        (3,'Ⅱ'),
        (4,'Ⅲ'),
        (5,'Ⅳ'),
    )
    site_type=models.SmallIntegerField(choices=site_classification_choice,default=1,verbose_name='场地类别')
    number=models.SmallIntegerField(verbose_name='地震波数')#地震波数
    group_choice=(
        (1,'第一组'),
        (2,'第二组'),
        (3,'第三组'),
    )
    group=models.SmallIntegerField(choices=site_classification_choice,default=1,verbose_name='地震分组')#地震分组
    
    #地震水准，分三种，多遇，设防，罕遇
    earthquake_level_choice=(
        (1,'多遇'),
        (2,'设防'),
        (3,'罕遇'),
    )
    earthquake_level=models.SmallIntegerField(choices=earthquake_level_choice,default=1,verbose_name='地震水准')
    #峰值加速度,用if，else判断，由地震水准和设防烈度唯一确定
    peak_acceleration=models.DecimalField(max_digits=12,decimal_places=6,verbose_name='峰值加速度')

def upload_to2(instance,filename):
    return '/'.join(['wave_file',instance.project,instance.earthquake_wave_no,filename])
class Earthquake_wave_detail(models.Model):
    '''地震波详情'''
    class Meta:
        verbose_name='地震波详情'
        verbose_name_plural='地震波详情'
    project=models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='项目',default=None)
     #指向Project的外键，一个project对应多个地震细节,
     #地震波编号，有多少个地震波，就有多少个地震波文件
    earthquake_wave_no=models.SmallIntegerField(verbose_name='地震波编号')
    #地震波名称
    earthquake_wave_name=models.CharField(max_length=256,verbose_name='地震波名称')
    #地震波峰值
    peak=models.DecimalField(max_digits=12,decimal_places=6,verbose_name='地震波峰值')
    #文件存放位置
    earthquake_wave_file=models.FileField(upload_to=upload_to2,verbose_name='地震波文件')

class Structure_response(models.Model):
    #django自己生成主键
    #指向Project的外键，一个project对应多个结构响应
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    #方向,分X,Y
    direction_choice=(
        ('X','X方向'),
        ('Y','Y方向'),
    )
    direction=models.CharField(max_length=1,choices=direction_choice,default='X')
    #EDP类型，分层间位移角和楼层加速度
    EDP_type_choice=(
        ('S','层间位移角/Story Drift Ratio'),#层间位移角
        ('A','楼层加速度/Acceleration'),#楼层加速度
    )
    EDP_type=models.CharField(max_length=1,choices=EDP_type_choice,default='S')
    #指向DB_type的外键，一个结构构件对应一个结构类型
    class Meta:
        unique_together=('project','direction','EDP_type')        
        verbose_name='结构响应'
        verbose_name_plural='结构响应' 
    #楼层数量决定表的宽度，地震数量决定表的长度
    floor_no=models.SmallIntegerField(verbose_name='楼层数量')
    earthquake_no=models.SmallIntegerField(verbose_name='地震波数量')
    data=models.CharField(max_length=10240,verbose_name='序列化的数组')





from django.contrib import admin
from BTESDB.models import *
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('username','truename', 'company','date_joined','last_login','is_superuser','is_active')
    
    #fk_fields 设置显示外键字段
    fk_fields = ('company',)

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10

    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('date_joined',)

     #list_editable 设置默认可编辑字段
    list_editable = ['is_active',]

    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('username', 'truename')

    list_filter =('company__com_name',) #过滤器
    date_hierarchy = 'date_joined'    # 详细时间分层筛选
    search_fields =('username','truename','company__com_name',) #搜索字段
admin.site.register(User_Info,UserInfoAdmin)

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display=('com_name','certificate','total_user','com_tel','fax','address')
    list_per_page=50
    ordering=('com_name',)
admin.site.register(Company_Info,CompanyInfoAdmin)

class DB_partAdmin(admin.ModelAdmin):
    list_display=('part_id','part_name','description','EDP_type','data_resource','is_formal','part_type')
    list_per_page=50
    ordering=('part_id',)
admin.site.register(DB_part,DB_partAdmin)

class ProjectAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """函数作用：使当前登录的用户只能看到自己新建的项目"""
        print (1)
        qs = super(ProjectAdmin, self).get_queryset(request)
        print(2)
        if request.user.is_superuser:
            print(3)
            return qs
        print(4)
        return qs.filter(user=User_Info.objects.filter(username=request.user))
 
    list_display = ('user', 'project_name','client_name','last_update','create_time','is_finished','rate')
admin.site.register(Project,ProjectAdmin)

'''
class DB_userAdmin(admin.ModelAdmin):
    list_display=('User','self_id','self_name','self_description','EDP_type','self_create_time')
    list_per_page=50
    ordering=('User','self_id',)
    date_hierarchy = 'self_create_time'    # 详细时间分层筛选
admin.site.register=(DB_user,DB_userAdmin)'''
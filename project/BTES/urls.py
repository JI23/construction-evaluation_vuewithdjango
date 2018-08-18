"""BTES URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BTESDB import views
from BTESDB import user_login
from BTESDB import register
from BTESDB import project
from BTESDB import floor
from BTESDB import show_all
from BTESDB import earthquake_info
from BTESDB import wave
from BTESDB import structure_response
from django.conf.urls import url,include
from django.views.generic import TemplateView
import BTESDB.urls

admin.autodiscover()
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/', include(BTESDB.urls)),

    path('admin/', admin.site.urls),

    path('',views.index),

    path('user_register/',register.user_register),
    path('admin_register/',register.admin_register),
    path('company_register/',register.company_register),
    path('login/',user_login.login),
    path('logout/',views.logout),
    path('insert/',project.insert),
    path('ist/',project.ist),


    path('new_project/',project.one_project),
    path('new_project2/',project.two_project),
    path('new_project3/',floor.three_floor),
    path('new_project4/',show_all.save_structure),
    path('new_project5/',show_all.save_nonstructure),
    path('new_project6/',earthquake_info.earthquake_info),
    path('new_project7/',wave.wave_info),
    path('new_project8/',structure_response.structure_response),
    path('all_part/',show_all.get_all_parts,name='all_part'),
    url(r'^new_project4/(?P<id>\d+)/$',show_all.show_selected_structure,name='new_project4'),
    url(r'^new_project5/(?P<id>\d+)/$',show_all.show_selected_nonstructure,name='new_project5'),
]

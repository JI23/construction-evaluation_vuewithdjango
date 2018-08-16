from django.contrib import admin
from . import *
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'add_book$', views.add_book, ),
    url(r'show_projects$', views.show_projects, ),
    ]
from django.contrib import admin
from . import views,step1,step2,step3
from . import step5,step6,user_login,register
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'step1$', step1.step1, ),
    url(r'step2$', step2.step2, ),
    url(r'step2-saveFloor$', step2.saveFloor, ),
    url(r'step3-get-all-parts$', step3.get_all_parts, ),
    url(r'step3-save-elements$', step3.save_elements, ),
    url(r'step5$', step5.step5 ),
    url(r'step5-save-waves$', step5.save_waves ),
    url(r'step6$', step6.step6 ),
    url(r'show_projects$', views.show_projects, ),
    url(r'login$', user_login.login ),
    url(r'user_register$', register.user_register ),
    ]
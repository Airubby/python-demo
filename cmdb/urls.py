
from django.contrib import admin
from django.urls import re_path
from cmdb import views

urlpatterns = [

    re_path('login',views.login),
    re_path('index',views.index),
    re_path('user_info', views.user_info),
    re_path('userdetail-(?P<nid>\d+)', views.user_detail),
    re_path('userdel-(?P<nid>\d+)', views.user_del),
    re_path('useredit-(?P<nid>\d+)', views.user_edit),
]




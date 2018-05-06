
from django.urls import re_path
from app02 import views

urlpatterns = [
    re_path('tpl$',views.tpl),
    re_path('tpl1$',views.tpl1),
    re_path('tpl2$',views.tpl2),
    re_path('tpl3$',views.tpl3),
    re_path('user_list',views.user_list),
    re_path('login',views.login),
    re_path('home',views.home),
]




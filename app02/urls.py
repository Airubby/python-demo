
from django.urls import re_path
from app02 import views
app_name='app02'

urlpatterns = [
    re_path('index$',views.index,{'name':'xie'},name="index"),
    re_path('tpl$',views.tpl),
re_path('tpl1$',views.tpl1),
re_path('tpl2$',views.tpl2),
re_path('tpl3$',views.tpl3),
]




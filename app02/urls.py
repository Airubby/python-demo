
from django.urls import re_path
from app02 import views
app_name='app02'

urlpatterns = [
    re_path('index$',views.index,{'name':'xie'},name="index"),
]




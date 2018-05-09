"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path,include


"""
#如果多个模块的views引入，这样就不好，因为每个模块分工开发的时候要修改url都要来这个页面，冲突或者
#重复的问题就有了
#from cmdb import views
urlpatterns = [
    re_path('admin/', admin.site.urls),
    # path('home', views.home),
    re_path('login',views.login),
    re_path('home', views.Home.as_view()), #as_view()固定写法
    re_path('index',views.index,name='indexform'),
    #path('detail/',views.detail), #以?传参显示
    #re_path('detail-(\d+)',views.detail),  #不以?传参显示 re_path('detail-(\d+).html',views.detail), 然后url跳转时也加.html
    re_path('detail-(?P<nid>\d+)',views.detail), #这样传参views.py中就匹配nid的参数，无论形式参数先后顺序，传多个参数
]
"""
from app03 import views

urlpatterns=[
    re_path('admin/', admin.site.urls),
    re_path('cmdb', include("cmdb.urls")),
    re_path('app01', include("app01.urls")),
    re_path('app02', include("app02.urls")),

    #re_path('a', include("app02.urls",namespace='author')),  #命名空间
    re_path('login$', views.login),
    re_path('index$', views.index),
    re_path('logout$', views.logout),
    re_path('test$', views.test),   #测试中间件
    re_path('cache$', views.cache),
]


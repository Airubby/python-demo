
from django.contrib import admin
from django.urls import re_path
from cmdb import views

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




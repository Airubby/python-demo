
from django.urls import re_path
from app01 import views

urlpatterns = [
    re_path('login',views.login),
    re_path('business$',views.business),  #给$终止符，不然后面如果还有还有包含business（比如：business_add）就不会执行了
    re_path('business_add',views.business_add),
    re_path('host$',views.host),
    re_path('test_ajax$',views.test_ajax),
]




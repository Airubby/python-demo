#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Airubby 
@file: m1.py 
@time: 2018/05/08 
"""
#Middle文件夹随便命名，写了中间件还得在settings中注册

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('第一个中间件,网申')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('1张星童')

    def process_response(self,request,response):  #参数顺序及字段就是这样的，django只识别process_response这个函数
        print('返回了第一个中间件，张坤')
        return response



class Row2(MiddlewareMixin):
    def process_request(self, request):
        print('第二个中间件')
        #return HttpResponse('这里有response了，就不会执行后面的中间件了')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('2彰显')

    def process_response(self,request,response):
        print('返回了2')
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print('第三个中间件')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('3下小戴')

    def process_response(self,request,response):
        print('返回了3')
        return response

    def process_exception(self,request,exception):
        print("views中函数出错了才执行这个")
        if isinstance(exception,ValueError):
            return HttpResponse("出错了")














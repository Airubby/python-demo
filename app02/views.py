from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request,name):
    print(name)
    return HttpResponse("ok")






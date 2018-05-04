from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request,name):
    print(name)
    v =reversed('author:index')   #namespace='author' app下面的url，感觉命名空间没用
    print(v)

    print(request.environ)
    for k,v in request.environ.items():
        print(k,v)
    #HTTP_USER_AGENT，获取终端是什么，不同终端反应不同页面
    print(request.environ['HTTP_USER_AGENT'])
    return HttpResponse("ok")


def tpl(request):
    user_list=[1,2,3]
    return render(request, 'app02/tpl.html',{'u':user_list})
def tpl1(request):
    name='root'
    return render(request, 'app02/tpl1.html',{'name':name})
def tpl2(request):
    status="已删除"
    return render(request, 'app02/tpl2.html',{'status':status})
def tpl3(request):
    return render(request, 'app02/tpl3.html')



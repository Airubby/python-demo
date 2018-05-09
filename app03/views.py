from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
#每个函数上面加@csrf_exempt表示需要安全验证
#每个函数上面加@csrf_protect表示不需要安全验证
#这是对单个设置的，全局设置在settings中MIDDLEWARE的'django.middleware.csrf.CsrfViewMiddleware',表示开启安全验证


# Create your views here.

def login(request):

    from django.conf import settings
    print(settings.CSRF_HEADER_NAME)
    #HTTP_X_CSRFTOKEN，HTTP_是django加的所以传X-CSRFtoken，请求头不能有下划线

    if request.method=='GET':
        return render(request,'app03/login.html')
    elif request.method=='POST':
        user=request.POST.get("username")
        pwd = request.POST.get("password")
        if user=='root' and pwd =="xie123":
            #生成水机字符串；写到用户浏览器cookie；保存到session中
            #在随机字符串对应的字典中设置相关内容
            request.session['username']=user
            request.session['is_login']=True

            if request.POST.get('rmb',None)=='1':
                #10秒超时时间，默认是2周
                request.session.set_expiry(10)

            return redirect('/index')
        else:
            return render(request, 'app03/login.html')

def index(request):
    #del request.session['is_login']
    #request.session.delete('session_key')  删除所有的信息
    #request.session.clear()
    #request.session['is_login'] 不存在就要报错
    #获取当前用户的随机字符串，根据随机字符串获取对应的信息
    if request.session.get('is_login',None):
        #return HttpResponse('OK'+request.session['username'])
        return render(request,'app03/index.html')
    else:
        return HttpResponse('滚')


def logout(request):
    request.session.clear()   #清除所有
    return redirect('/login')


def test(request):
    #int('afsadf')  #测试出错执行中间件
    print("到最终了，----")
    return HttpResponse("中间件")


from django.views.decorators.cache import cache_page
#对单个函数做缓存
#@cache_page(10)   #缓存10秒，这个的优先级比。。高
def cache(request):
    import time
    ctime=time.time()
    return render(request,'app03/cache.html',{"ctime":ctime})



def signal(reuqest):
    from app03 import models

    obj = models.UserInfo(user='root')
    print('end')
    obj.save()

    obj = models.UserInfo(user='root')
    obj.save()

    obj = models.UserInfo(user='root')
    obj.save()

    # 自定义信号
    from sg import pizza_done
    pizza_done.send(sender="asdfasdf",toppings=123, size=456)
    # 自定义信号

    return HttpResponse('ok')




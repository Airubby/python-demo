from django.shortcuts import render,HttpResponse,redirect

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
    name="YSDFLSFLAsfsfdf"
    return render(request, 'app02/tpl3.html',{'name':name})


from utils import pagination

LIST=[]
for i in range(1009):
    LIST.append(i)
def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page=int(current_page)

    val=request.COOKIES.get('per_page_count')
    val=int(val)
    page_obj=pagination.Page(current_page,len(LIST),val)
    data=LIST[page_obj.start:page_obj.end]


    page_str=page_obj.page_str("/app02/user_list")
    return render(request,'app02/user_list.html',{"li":data,"page_str":page_str})



##################### cookie ############################

user_info={
    'dachengzi':{'pwd':'123456'},
    'kangbazi':{'pwd':'kkk'},
}

def login(request):
    if request.method=='GET':
        return render(request,'app02/login.html')  #这个是templates下面的app02文件夹名
    if request.method=="POST":
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic=user_info.get(u)
        if not dic:
            return render(request,'app02/login.html')
        if dic['pwd']==p:
            res=redirect('app02/home')  #这个是app02模块的文件名
            res.set_cookie('usernamecook',u,max_age=10) #10秒后清空cookies
            return res

        else:
            return render(request,'app02/login.html')
    #return HttpResponse('OK')


def home(request):
    v=request.COOKIES.get('usernamecook')
    if not v:
        return redirect('app02/login')
    return render(request,'app02/home.html',{'current_user':v})

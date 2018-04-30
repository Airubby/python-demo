from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from cmdb import models



def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        #获取用户通过POST提交过来的信息
        #username=request.POST['username']
        user=request.POST.get('username',None)
        passw = request.POST.get('password', None)

        obj=models.UserInfo.objects.filter(username=user,password=passw).first()
        if obj:
            return redirect('/cmdb/index')
        else:
            return render(request,'login.html')
    return render(request,'login.html',{'error_msg':error_msg})


def index(request):
    return render(request,'index.html')

def user_info(request):
    user_list=models.UserInfo.objects.all()
    return render(request, 'user_info.html',{'user_list':user_list})

def user_detail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    #models.UserInfo.objects.get(id=nid) #区单挑数据如果不存在则报错
    return render(request, 'user_detail.html', {'obj': obj})

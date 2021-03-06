from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from cmdb import models



def login(request):
    models.UserGroup.objects.create(caption='DBA')
    if request.method=="GET":
        return render(request, 'app01/login.html')
    elif request.method=="POST":
        #获取用户通过POST提交过来的信息
        #username=request.POST['username']
        user=request.POST.get('username',None)
        passw = request.POST.get('password', None)

        obj=models.UserInfo.objects.filter(username=user,password=passw).first()
        if obj:
            return redirect('/cmdb/index')
        else:
            return render(request, 'app01/login.html')
    return render(request, 'app01/login.html', {'error_msg':error_msg})


def index(request):
    return render(request, 'app01/index.html')

def user_info(request):
    if request.method=='GET':
        user_list=models.UserInfo.objects.all()
        group_list=models.UserGroup.objects.all()
        return render(request, 'app01/user_info.html', {'user_list':user_list, 'group_list':group_list})
    elif request.method=='POST':
        user=request.POST.get('username')
        passw = request.POST.get('password')
        models.UserInfo.objects.create(username=user,password=passw)
        return redirect('/cmdb/user_info')

def user_detail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    #models.UserInfo.objects.get(id=nid) #区单挑数据如果不存在则报错
    return render(request, 'app01/user_detail.html', {'obj': obj})

def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info')

def user_edit(request,nid):
    if request.method=='GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'app01/user_edit.html', {'obj':obj})
    elif request.method=='POST':
        nid=request.POST.get('id')
        user = request.POST.get('username')
        passw = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=user,password=passw)
        return redirect('/cmdb/user_info')

def orm(request):
    return HttpResponse("OK")
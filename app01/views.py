from django.shortcuts import render,HttpResponse
from app01 import models

# Create your views here.
def login(request):
    # f = open('templates/login.html', 'r', encoding='utf-8')
    # data = f.read();
    # f.close()
    # return HttpResponse(data)
    error_msg=""
    if request.method=="POST":
        #获取用户通过POST提交过来的信息
        #username=request.POST['username']
        username=request.POST.get('username',None)
        password = request.POST.get('password', None)
        gender=request.POST.get('gender',None)
        favor = request.POST.getlist('favor', None)
        #file = request.POST.get('fileinfo', None)
        file=request.FILES.get('fileinfo')
        import os
        file_path=os.path.join('upload',file.name)
        print(file_path)
        f=open(file_path,mode="wb")
        for i in file.chunks():
            f.write(i)
        f.close()
        if username=="admin" and password=="xie123":
            return redirect('/home')
        else:
            error_msg="用户名或密码错误"
    return render(request,'login.html',{'error_msg':error_msg})

def business(request):
    v1=models.Business.objects.all()
    #QuerySet
    #[obj(id,caption,code),obj(id,caption,code),obj(id,caption,code)]
    v2=models.Business.objects.all().values('id','caption')
    # QuerySet
    # [{'id':1,'caption':'运营部'},{'id':1,'caption':'运营部'},{'id':1,'caption':'运营部'}]
    v3 = models.Business.objects.all().values_list('id', 'caption')
    # QuerySet
    # [(1,'运营部'),(2,'运营部')]

    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})

def business_add(request):
    return HttpResponse("OK")


def host(request):
    v1 = models.Host.objects.filter(nid__gt=0)  #nid>0 等价于.all()

    v2=models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
    #字典跨表要用__（b__caption）
    v3=models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')
    return render(request, 'host.html', {'v1': v1,'v2':v2,'v3':v3})

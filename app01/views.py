from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import json
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

    if request.method=='GET':
        v1 = models.Host.objects.filter(nid__gt=0)  #nid>0 等价于.all()
        v2=models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
        #字典跨表要用__（b__caption）
        v3=models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')

        b_list=models.Business.objects.all()

        return render(request, 'host.html', {'v1': v1,'v2':v2,'v3':v3,'b_list':b_list})
    elif request.method=="POST":
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(hostname=h,
                                   ip=i,
                                   port=p,
                                   b_id=b
                                   )
        return redirect('/app01/host')


def test_ajax(request):
    #print(request.method,request.POST.get('user'),request.GET.get('pwd'),sep='\t')

    ret={'status':True,'error':None,'data':None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) > 5:
            models.Host.objects.create(hostname=h,
                                       ip=i,
                                       port=p,
                                       b_id=b
                                       )
        else:
            ret['status']=False
            ret['error']="太短了"
    except Exception as e:
        ret['status'] = False
        ret['error'] = "请求错误"

    return HttpResponse(json.dumps(ret))  #序列化


def application(request):
    if request.method=="GET":

        app_list=models.Application.objects.all()
        host_list=models.Host.objects.all()
        return render(request,'app.html',{"app_list":app_list,'host_list':host_list})
    elif request.method=="POST":
        app_name=request.POST.get('app_name')
        host_list=request.POST.getlist('host_list')

        obj=models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)

        return redirect('/app01/application')


def ajax_add_app(request):
    ret={'status':True,'error':None,'data':None}
    print(request.POST.get('app_name'))
    print(request.POST.get('host_list'))
    app_name = request.POST.get('app_name')
    host_list = request.POST.getlist('host_list')

    obj = models.Application.objects.create(name=app_name)
    obj.r.add(*host_list)

    return HttpResponse(json.dumps(ret))












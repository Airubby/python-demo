from django.shortcuts import render

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

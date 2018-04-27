from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.shortcuts import HttpResponse


# def login(request):
#     # f = open('templates/login.html', 'r', encoding='utf-8')
#     # data = f.read();
#     # f.close()
#     # return HttpResponse(data)
#     error_msg=""
#     if request.method=="POST":
#         #获取用户通过POST提交过来的信息
#         #username=request.POST['username']
#         username=request.POST.get('username',None)
#         password = request.POST.get('password', None)
#         print(username,password)
#         if username=="admin" and password=="xie123":
#             return redirect('/home')
#         else:
#             error_msg="用户名或密码错误"
#     return render(request,'login.html',{'error_msg':error_msg})

USER_LIST=[
    {'id':111,'username':'airubby','email':'airubby@qq.com','gender':'man'},
]
for index in range(2):
    temp={'id':index,'username':'airubby'+str(index),'email':'airubby@qq.com','gender':'man'}
    USER_LIST.append(temp)

def home(request):
    username = request.POST.get('username', None)
    email = request.POST.get('email', None)
    gender = request.POST.get('gender', None)
    temp={'id':username,'username':username,'email':email,'gender':gender}
    USER_LIST.append(temp)
    return render(request, 'home.html',{"user_list":USER_LIST})


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

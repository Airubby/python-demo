from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def login(request):
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
            return redirect(index)
        else:
            return render(request, 'app03/login.html')

def index(request):
    #获取当前用户的随机字符串，根据随机字符串获取对应的信息
    if request.session['is_login']:
        return HttpResponse('OK'+request.session['username'])
    else:
        return HttpResponse('滚')
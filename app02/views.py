from django.shortcuts import render,HttpResponse
from django.utils.safestring import mark_safe
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


LIST=[]
for i in range(109):
    LIST.append(i)
def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page=int(current_page)
    start=(current_page-1)*10
    end=current_page*10
    data=LIST[start:end]

    all_count = len(LIST)
    count,y=divmod(all_count,10)
    if y:
        count+=1

    page_list=[]
    for i in range(1,count+1):
        if i==current_page:
            temp='<a class="page active" href="/app02/user_list/?p=%s">%s</a>' %(i,i)
        else:
            temp = '<a class="page" href="/app02/user_list/?p=%s">%s</a>' % (i, i)
        page_list.append(temp)

    page_str="".join(page_list)
    page_str=mark_safe(page_str)  #设置html，js代码信任，不然会以字符串显示

    return render(request,'app02/user_list.html',{"li":data,"page_str":page_str})




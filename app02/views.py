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
for i in range(1009):
    LIST.append(i)
def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page=int(current_page)
    per_page_cout=10
    pager_num = 5

    start=(current_page-1)*per_page_cout
    end=current_page*per_page_cout
    data=LIST[start:end]

    all_count = len(LIST)
    total_count,y=divmod(all_count,per_page_cout)
    if y:
        total_count+=1

    page_list=[]

    # start_index=current_page-5
    # end_index=current_page+6  #区间含头部含尾
    if total_count<pager_num:
        start_index=1
        end_index=total_count+1
    else:
        if current_page <=(pager_num+1)/2:
            start_index=1
            end_index=pager_num+1
        else:
            start_index = current_page - (pager_num-1)/2
            end_index = current_page + (pager_num+1)/2
            if (current_page+(pager_num-1)/2)>total_count:
                start_index = total_count - pager_num+1
                end_index = total_count+1
    if current_page==1:
        prev = '<a class="page" href="javascript:;">上一页</a>'
    else:
        prev = '<a class="page" href="/app02/user_list/?p=%s">上一页</a>' % (current_page - 1)

    page_list.append(prev)
    for i in range(int(start_index),int(end_index)):
        if i==current_page:
            temp='<a class="page active" href="/app02/user_list/?p=%s">%s</a>' %(i,i)
        else:
            temp = '<a class="page" href="/app02/user_list/?p=%s">%s</a>' % (i, i)
        page_list.append(temp)
    if current_page==total_count:
        next = '<a class="page" href="javascript:;">下一页</a>'
    else:
        next = '<a class="page" href="/app02/user_list/?p=%s">上一页</a>' % (current_page + 1)
    page_list.append(next)

    jump="""
        <input type='text' /><a onclick='jumpTo(this,"/app02/user_list/?p=");' id='go'>GO</a>
        <script>
            function jumpTo(_this,base){
                var val=_this.previousSibling.value;
                location.href=base+val;
            }
        </script>
    """
    page_list.append(jump)
    page_str="".join(page_list)
    page_str=mark_safe(page_str)  #设置html，js代码信任，不然会以字符串显示

    return render(request,'app02/user_list.html',{"li":data,"page_str":page_str})




from django.shortcuts import render,HttpResponse
from django import forms
#from django.forms import fields  #UserInfoForm中用的，可以不用别名
from django.forms import fields as Ffields

from django.forms import widgets as Fwidgets   #设置别名是因为和下面的widgets重名了

from publicapp import models



# Create your views here.

# class UserInfoForm(forms.Form):
#     username=fields.CharField(max_length=32)
#     email=fields.EmailField()
#     user_type=fields.ChoiceField(
#         choices=models.UserType.objects.values_list('id','caption')
#     )
#
#     #更新操作
#     def __init__(self, *args, **kwargs):
#         super(UserInfoForm, self).__init__(*args, **kwargs)
#         self.fields['user_type'].choices = models.UserType.objects.values_list('id', 'caption')
#
#
# def index(request):
#     if request.method=="GET":
#         obj=UserInfoForm()
#         return render(request, 'index.html',{'obj':obj})
#     elif request.method=='POST':
#         obj=UserInfoForm(request.POST)
#         obj.is_valid()
#         obj.errors()
#         #新增
#         # models.UserInfo.objects.create(**obj.cleaned_data)
#         #更新
#         # models.UserInfo.objects.filter(id=1).update(**obj.cleaned_data)
#         return render(request,'index.html',{'obj':obj})
#

#以上是基于form的新增修改，以下是基于ModelForm

class UserInfoModelForm(forms.ModelForm):

    mianmi=Ffields.CharField(  #不写库的字段，比如保存session，几天免密登录这些，然后再下面mf.save()保存之前做操作
        widget=Fwidgets.CheckboxInput()
    )

    class Meta:
        model=models.UserInfo
        fields='__all__'   #全部字段显示
        #fields=['username','email']
        #exclude=['user_type']   #除去user_type以外的字段

        labels={
            'email':'邮箱'
        }
        help_texts={
            'username':'username的help信息'
        }
        widgets={
            'username':Fwidgets.Textarea(attrs={'class':'cname'})
        }
        error_messages={
            '__all__':{
                #整体的错误信息
            },
            'email':{
                'required':'密码不能为空',
                'invalid':'邮箱格式错误'
            }
        }
        field_classes={
            #'username':Ffields.URLField  #fields用as 别名Ffields，因为冲突了
        }

    def clean_username(self):  #对username进行验证，得有返回值
        old=self.cleaned_data['username'] #获取原来的值
        #这个地方对原来的值进行操作，然后返回
        return old

def index(request):
    if request.method=="GET":
        obj=UserInfoModelForm()
        return render(request, 'index.html',{'obj':obj})
    elif request.method=='POST':
        obj=UserInfoModelForm(request.POST)
        if obj.is_valid():
            #obj.save()  #保存所有
            #下面的不会保存多对多关系的
            instance=obj.save(False)
            instance.save()
            obj._save_m2m()  #这个是保存多对多，这样才和obj.save()保存同样操作了
        return render(request, 'index.html',{'obj':obj})



def user_list(request):
    li = models.UserInfo.objects.all().select_related('user_type')
    return render(request,'user_list.html',{'li': li})

def user_edit(request, nid):
    if request.method == "GET":
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)  #生成标签
        return render(request,'user_edit.html',{'mf': mf, 'nid': nid})
    elif request.method == 'POST':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST,instance=user_obj)  #加上instance=user_obj才是对这条数据更新，而不是新增一条信息
        if mf.is_valid():
            #没写库的字段做操作
            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request,'user_edit.html',{'mf': mf, 'nid': nid})


def upload(request):

    return render(request,'upload.html')

def upload_file(request):
    username=request.POST.get('username')
    filename=request.FILES.get('filename')
    print(username,filename)
    import os
    img_path = os.path.join('static/images/', filename.name)
    with open(img_path, 'wb') as f:
        for item in filename.chunks():
            f.write(item)
    ret = {'code': True, 'data': img_path}
    import json
    return HttpResponse(json.dumps(ret))








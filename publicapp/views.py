from django.shortcuts import render,HttpResponse
from django import forms
from django.forms import fields
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
    class Meta:
        model=models.UserInfo
        fields='__all__'   #全部字段显示
        #fields=['username','email']
        #exclude=['user_type']   #除去user_type以外的字段


def index(request):
    if request.method=="GET":
        obj=UserInfoModelForm()
        return render(request, 'index.html',{'obj':obj})
    elif request.method=='POST':
        obj=UserInfoModelForm(request.POST)
        print(obj.is_valid())
        print(obj.cleaned_data)
        print(obj.errors)
        return render(request, 'index.html',{'obj':obj})



















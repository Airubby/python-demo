from django.db import models


#要在setting中INSTALLED_APPS添加那个模块，比如'cmdb'模块
#然后在migrations下生成执行文件：python manage.py makemigrations
#然后生成数据库：python manage.py migrate
class UserInfo(models.Model):
    username=models.CharField(max_length=32,blank=True)
    password=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    test = models.EmailField(max_length=32, null=True)

    user_type_choice=(
        (1,'超级用户'),
        (2, '普通用户'),
        (3, '一般用户'),
    )
    user_type_id=models.IntegerField(choices=user_type_choice,default=1)


class UserGroup(models.Model):
    uid=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=32)
    ctime=models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)

    # uptime更新时间只有用下面的方法才会自动更新时间
    # obj=UserGroup.objects.filter(id=1).first()
    # obj.caption="CEO"
    # obj.save()

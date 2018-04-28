from django.db import models


#要在setting中INSTALLED_APPS添加那个模块，比如'cmdb'模块
#然后在migrations下生成执行文件：python manage.py makemigrations
#然后生成数据库：python manage.py migrate
class UserInfo(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
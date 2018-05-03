from django.db import models

# Create your models here.



class Business(models.Model):
    caption=models.CharField(max_length=32)
    code=models.CharField(max_length=32,null=True,default="SA") #后面新增的，可以直接先附上默认值，或者给可以为空


class Host(models.Model):
    nid=models.AutoField(primary_key=True)
    hostname=models.CharField(max_length=32,db_index=True)
    ip=models.GenericIPAddressField(protocol="ipv4",db_index=True)  #ipv4 默认是both protocol="both"
    port=models.IntegerField()
    b=models.ForeignKey(to="Business",to_field='id',on_delete=models.CASCADE)

class Application(models.Model):
    name=models.CharField(max_length=32)
    r=models.ManyToManyField("Host")  #写了这个就不用写自定义关系表了，django自动创建，这个只能写一个
    #自定义可以写多个，自定义比较推荐

#多对多，自定义关系表
# class HostToApp(models.Model):
#     hobj=models.ForeignKey(to='Host',to_field='nid',on_delete=models.CASCADE)
#     aobj=models.ForeignKey(to='Application',to_field='id',on_delete=models.CASCADE)











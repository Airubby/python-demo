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
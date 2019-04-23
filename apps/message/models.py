from django.db import models

# Create your models here.

class FromTable(models.Model):
    #下面是定一个一个自定义名称主键，在属性primary_key=True时，说明此变量取代主键
    object_id = models.CharField(max_length=50,default='',primary_key=True)
    #定义姓名表的属性，长度，是否为空，默认值，备注信息等
    username = models.CharField(max_length=20,null =True,blank=True, default='',verbose_name=u"姓名")
    email = models.EmailField(max_length=20,verbose_name=u"邮箱")
    adsress = models.CharField(max_length=100,verbose_name=u"地址")
    message = models.CharField(max_length=500,verbose_name=u"信息")

    # class Meta:
    #     verbose_name = u'用户信息'
    #     verbose_name_pluralv = verbose_name


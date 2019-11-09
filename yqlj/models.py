from django.db import models

# Create your models here.

class yqlj_models(models.Model):
    # id = models.IntegerField('序号',primary_key=True)
    yqlj_name = models.CharField('博客名称',max_length=50)
    yqlj_urllist = models.CharField('博客地址',max_length=50)

    def __str__(self):
        return self.yqlj_name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
            


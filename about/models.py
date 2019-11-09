from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class About(models.Model):
    # id = models.IntegerField('序号',primary_key=True)
    about_context = RichTextUploadingField('个人简介-详情')

    def __str__(self):
        about_title = ''
        return about_title
    class Meta:
        verbose_name = '个人简介'
        verbose_name_plural = verbose_name
            
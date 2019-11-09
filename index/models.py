from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Index_Information(models.Model):
    title = models.CharField('博客标题名称①',max_length=50)
    title_name = models.CharField('博客标题名称②',max_length=50)
    Description = models.CharField('博客相关内容关键信息',max_length=50)

    def __str__(self):
        Index_Information_title = '网站基础配置信息'
        return Index_Information_title
    class Meta:
        #如只设置verbose_name，在Admin会显示为"产品信息s"
        verbose_name = '博客标题'
        verbose_name_plural = verbose_name


class Index_Body(models.Model):
    # id = models.IntegerField('文章序号',primary_key=True)
    blog_body_name = models.CharField('文章名称',max_length=50)
    blog_body_time = models.DateTimeField('文章发布时间')
    blog_body_context = RichTextUploadingField('文章内容')
    blog_body_type_1 = models.CharField('文章类型',max_length=15)
    blog_body_type_2 = models.CharField('文章标签',max_length=15)

    def __str__(self):
        return self.blog_body_name

    class Meta:
        #如只设置verbose_name，在Admin会显示为"产品信息s"
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name








from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title = '博客后台管理'
admin.site.site_header = '我的博客'

@admin.register(Index_Information)
class Index_Information_Admin(admin.ModelAdmin):
    #设置显示的字段
    list_display = ['title', 'title_name','Description',]

@admin.register(Index_Body)
class Index_Body_Admin(admin.ModelAdmin):
    #设置显示的字段
    list_display = ['id', 'blog_body_name', 'blog_body_time','blog_body_type_1','blog_body_type_2',]


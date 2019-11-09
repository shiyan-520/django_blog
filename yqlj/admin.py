from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(yqlj_models)
class Yqlj_Models_Admin(admin.ModelAdmin):
    #设置显示的字段
    list_display = ['id','yqlj_name', 'yqlj_urllist',]

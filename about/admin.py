from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(About)
class Blog_About_Admin(admin.ModelAdmin):
    #设置显示的字段
    list_display = ['id','about_context',]

from django.apps import AppConfig

# 填写 apps.py 中的类名称
default_app_config = 'index.IndexConfig'

class IndexConfig(AppConfig):
    name = 'index'
    verbose_name = '博客标题与博客文章-设置'
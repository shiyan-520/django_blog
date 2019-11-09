from django.apps import AppConfig

# 填写 apps.py 中的类名称
default_app_config = 'yqlj.YqljConfig'

class YqljConfig(AppConfig):
    name = 'yqlj'
    verbose_name = '友情链接-设置'
from django.apps import AppConfig


default_app_config = 'about.AboutConfig'

class AboutConfig(AppConfig):
    name = 'about'
    verbose_name = '个人简介-设置'

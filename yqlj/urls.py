from django.urls import path
from . import views

urlpatterns = [
    path('',views.Yqlj_Url,name='yqlj_url'),
]


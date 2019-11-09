from django.urls import path
from . import views


urlpatterns = [
    path('', views.Posts_list,name='posts_list'),
]



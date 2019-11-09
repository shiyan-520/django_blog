from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_About, name="blog_About"),
]
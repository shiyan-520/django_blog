from django.urls import path
from . import views


urlpatterns = [
    path('<int:blog_pk>', views.blog_Article, name="blog_Article"),
]
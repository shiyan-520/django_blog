from django.shortcuts import render,get_object_or_404
from index.models import *

# Create your views here.

def blog_Article(request,blog_pk):
    index_information = Index_Information.objects.get(pk=1)
    index_body = get_object_or_404(Index_Body, pk=blog_pk)
    return render(request, 'blog_article.html', locals())


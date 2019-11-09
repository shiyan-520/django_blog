from django.shortcuts import render
from .models import *
from index.models import *

# Create your views here.

def blog_About(request):
    index_information = Index_Information.objects.get(pk=1)
    index_about = About.objects.get(pk=1)
    return render(request,'about.html',locals())


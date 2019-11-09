from django.shortcuts import render
from .models import *
from index.models import *

# Create your views here.

def Yqlj_Url(request):
    index_information = Index_Information.objects.get(pk=1)
    yqlj_context = yqlj_models.objects.all()
    return render(request,'yqlj.html',locals())

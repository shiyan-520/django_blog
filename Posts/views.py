from django.shortcuts import render
from index.models import *
# Create your views here.


def Posts_list(request):
    index_information = Index_Information.objects.get(pk=1)
    index_body = Index_Body.objects.all().order_by("-id")
    return render(request,'Posts_list.html',locals())



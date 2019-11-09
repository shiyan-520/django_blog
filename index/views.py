from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def index_paging(request):
    # 等闲了就总结总结谢谢注释
    index_information = Index_Information.objects.get(pk=1)
    cus_list = Index_Body.objects.all().order_by("-id")
    paging_list = Paginator(cus_list,6,1) # 这里用来设置首页显示多少文章
    page = request.GET.get('page')
    try:
        customer = paging_list.page(page)
    except PageNotAnInteger:
        customer = paging_list.page(1)
    except EmptyPage:
        customer = paging_list.page(paging_list.num_pages)
    return render(request,'index1.html',{"cus_list":customer,"index_information":index_information,})





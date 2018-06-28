from django.shortcuts import render,get_list_or_404
from .models import Ablum,Pic
import json
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def index(request):
    ablum = get_list_or_404(Ablum)
    pagniator = Paginator(ablum,15)
    page = request.GET.get('page')

    try:
        ablum_list = pagniator.page(page)
    except PageNotAnInteger:
        ablum_list = pagniator.page(1)
    except EmptyPage:
        ablum_list = pagniator.page(pagniator.num_pages)

   # ab_json = json.load(serializers.serialize("json",ablum_list))
    return  render(request,"bl/index.html",{ "ablum_list": ablum_list })


def detail(request,ablum_id):
    ablum = Ablum.objects.filter(id = ablum_id)[0]
    pic_list =  ablum.pic_set.all()
    paginator = Paginator(pic_list,3)
    page = request.GET.get("page")

    try:
        pic_list = paginator.page(page)
    except PageNotAnInteger:
        pic_list = paginator.page(1)
    except EmptyPage:
        pic_list = paginator.page(paginator.num_pages)

    return render(request,"bl/detail.html",{"ablum":ablum,"pic_list": pic_list})
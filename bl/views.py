from django.shortcuts import render,get_list_or_404
from .models import Ablum,Pic
import json

# Create your views here.
def index(request):
    ablum_list = get_list_or_404(Ablum)[-10:]
   # ab_json = json.load(serializers.serialize("json",ablum_list))
    return  render(request,"bl/index.html",{ "ablum_list": ablum_list })


def detail(request,ablum_id):
    ablum = Ablum.objects.filter(id = ablum_id)[0]
    pic_list =  ablum.pic_set.all()

    return render(request,"bl/detail.html/",{"ablum":ablum,"pic_list": pic_list})
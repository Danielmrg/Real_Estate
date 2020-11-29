from django.shortcuts import render , get_object_or_404
# from .filter import AdvertFilter
from .models import *

def home(request):
    advertising=Advertising.objects.publish()
    context = {
        'advertising': advertising,
    }
    return render(request,'home/advlist.html',context)

# def test(request):
#     adv=Advertising.objects.all()
#     filters=AdvertFilter(request.GET,queryset=adv)
#     context ={
#         'f':filters,
#     }
#     return render(request,'test/test.html',context)

# def detail_house(request,slug):
#     advert=Advertising.objects.publish()
#     house = get_object_or_404(advert,slug=slug)
#     context ={
#         'house':house,
#     }
#     return render(request,'home/detail_house.html',context)

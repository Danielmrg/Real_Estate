from django.shortcuts import render , get_object_or_404,redirect
from advertising.models import Advertising
from advertising.forms import AdvertForm
from extended.makeSlug import make_slug

# Create your views here.
def home(request):
    return render(request,'profile/index.html')

def all_advert(request):
    get_search=request.GET.get('search')
    if get_search != None:
        adverts=Advertising.objects.publish().filter(title__icontains=get_search)
    else:
        adverts=Advertising.objects.publish()
    context={
        'adverts':adverts,
    }
    return render(request,'profile/advert.html',context)

def detailview(request,slug):
    advert=Advertising.objects.publish()
    prod=get_object_or_404(advert,slug=slug)
    context={
        "advert":prod,
    }
    return render(request,'profile/detail.html',context)

def add_advert(request):
    user=request.user
    form=AdvertForm(request.POST or None,request.FILES or None,initial={'user':user})
    if form.is_valid():
        my_form=form.save()
        my_form.slug = make_slug()
        my_form.save()
        return redirect('account:home')
    context={
        'form':form,
    }
    return render(request,'profile/forms/forms.html',context)

def update_advert(request,slug):
    user=request.user
    advert=Advertising.objects.publish()
    instance=get_object_or_404(advert,slug=slug)
    if instance.user == user:
        form=AdvertForm(request.POST or None, request.FILES or None,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('account:home')
    else:
        return redirect('account:home')
    context={
        'form':form,
    }
    return render(request,'profile/forms/forms.html',context)

def adverts_estates(request):
    estate=request.user.estate
    

    context={

    }
    return render(request,'',context)



from django.shortcuts import render,redirect
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from advert.models import Advert
from authentication.models import User
from django.db.models import Q
from utils import get_by_pk_or_pass

def home(request):
    context = {
        'title':'خانه',
        "saleadverts":Advert.objects.public().filter(category="S"),
        "fullrentadverts":Advert.objects.public().filter(category="R"),
        "rentadverts":Advert.objects.public().filter(category="A"),
        "buyadverts":Advert.objects.public().filter(category="B"),
    }
    return render(request,"arti/Home.html",context)


def Adverts(request,page=1):
    page_number = page
    advertlist = Advert.objects.public()
    try:
        paginator = Paginator(advertlist, 6)
        adverts = paginator.get_page(page_number)
    except :
        adverts = ''
    context = {
        "title":"آگهی ها",
        "adverts":adverts
    }
    return render(request,"arti/Adverts.html",context)

def SearchAdvert(request,*args,**kwargs):
    search = request.GET
    data = dict(filter(lambda elem: elem[1] != None and elem[1] != '' and elem[1] !='0' ,search.items()))
    if not any(search.values()):
        return redirect("home:advert")
    adverts = Advert.objects.filter(is_active=True,is_public=True)
    if data.get('keyword'):
        lookup = (
            Q(title__icontains=data.get('keyword'))|
            Q(detail__icontains=data.get('keyword'))
        )
        adverts=adverts.filter(lookup).distinct()
    if data.get('category'):
        adverts = adverts.filter(category__iexact=data.get('category'))
    if data.get('status'):
        adverts = adverts.filter(statustype__iexact=data.get('status'))
    if data.get('types'):
        adverts = adverts.filter(house_type_iexact=data.get('types'))
    if data.get('property_bedrooms'):
        adverts = adverts.filter(beds__iexact=data.get('property_bedrooms'))
    if data.get('property_wc'):
        adverts = adverts.filter(wc__iexact=data.get('property_wc'))
    if data.get('min_price') and data.get('max_price'):
        adverts = adverts.filter(price__range=[int(data.get('min_price')),int(data.get('max_price'))])
    context = {
        "title":"search",
        'adverts': adverts,
    }
    return render(request, "arti/Adverts.html", context)

def DetailAdvert(request,Uid):
    try:
        advert = Advert.objects.get(Uid=Uid)
        title = advert.title
    except:
        advert = None
        title = "صفحه مورد نظر یافت نشد!"
    context = {
        "title":title,
        "advert":advert
    }
    return render(request,"arti/DetailAdvert.html",context)

def Agents(request,page=1):
    page_number = page
    agentlist = User.objects.get_by_role(role_name='agent')
    try:
        paginator = Paginator(agentlist, 6)
        agents = paginator.get_page(page_number)
    except :
        agents = ''
    context = {
        "title":"Agent's",
        "agents":agents,
    }
    return render(request,"arti/Agents.html",context)

def DetailAgent(request,pk):
    try:
      agent = User.objects.get(pk=pk)
    except:
      agent = None
    
    context = {
        "title":"Agent",
        "agent":agent,
    }
    return render(request,"arti/DetailAgent.html",context)
'''
def AboutUs(request):
    context = {
        "title":"About Us",
        "aboutus":None
    }
    return render(request,"",context)
'''
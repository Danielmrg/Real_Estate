from django.urls import path, include
from . import views


app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/all-advert/', views.all_advert, name='alladvert'),
    path('dashboard/detail/<slug:slug>/', views.detailview, name='detail'),
    path('dashboard/add-advert/',views.add_advert, name='add-advert'),
    path('dashboard/update_advert/<slug:slug>/',views.update_advert, name='update-advert'),
]

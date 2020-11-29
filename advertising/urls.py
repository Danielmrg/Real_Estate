from django.urls import path, include
from . import views

app_name = 'advertising'

urlpatterns = [
    path('',views.home,name='home'),
    # path('test/',views.test,name='test'),
    # path('details/<slug:slug>/',views.detail_house,name='detail_house'),
]
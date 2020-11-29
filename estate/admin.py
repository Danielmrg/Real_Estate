from django.contrib import admin
from .models import *

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    '''Admin View for Area'''

    list_display = ('title','code','status')
    list_filter = ('status',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    '''Admin View for Estate'''

    list_display = ('title','code')
    list_filter = ('status',)
    search_fields = ('title','code')
    ordering = ('-date_make',)
    prepopulated_fields = {'slug': ('title', )}
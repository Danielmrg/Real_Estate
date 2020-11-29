from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('title',)
    list_filter = ('status',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title', )}


class ImagesInline(admin.TabularInline):
    '''Tabular Inline View for Images'''
    model = Images
    min_num = 0
    max_num = 20
    extra = 1

class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('title','get_image_for_admin','status')    
    list_filter = ('status','send_in_estate','send_in_publish')
    inlines = [ImagesInline]
    search_fields = ('title','description')
    ordering = ('-date_added',)
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Advertising, AdvertisingAdmin)

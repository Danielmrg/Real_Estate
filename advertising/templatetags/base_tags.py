from django import template
from ..models import Category
# from ..filter import *

register = template.Library()

@register.inclusion_tag('home/include/nav.html')
def category_nav():
    return {
        'category': Category.objects.active(),
    }
from django import template
from advert.models import Advert

register = template.Library()

@register.simple_tag
def get_Advert():
    return Advert.objects.public()[:5]


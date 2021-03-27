from django import template
from home.models import company

register = template.Library()

@register.simple_tag
def get_company():
    return company.objects.all().first()
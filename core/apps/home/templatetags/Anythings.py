from django import template
import itertools
from authentication.models import User

register = template.Library()

@register.simple_tag
def get_agent():
    return User.objects.filter(role__title__iexact='agent')[:2]


__author__ = 'Administrator'
from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def addnum(a1, a2, a3):
    return a1+a2+a3


@register.simple_tag
def format(name):
    return 'format_'+name


@register.simple_tag
def my_getattr(item, attr):
    return getattr(item, attr)


@register.simple_tag
def iseque(v1, v2):
    v1 = str(v1)
    v2 = str(v2)
    if v1 == v2:
        return True
    else:
        return False

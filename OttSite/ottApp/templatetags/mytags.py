from django import template

register = template.Library()


# Template use:  { val|funcname:arg }
@register.filter
def subtract(value, arg):
    return value - arg

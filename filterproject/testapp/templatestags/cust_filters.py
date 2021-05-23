from django import template
register = template.Library()

@register.filter(name='truncaten')
def truncaten(value,n):
    result = value[0:n]
    return result

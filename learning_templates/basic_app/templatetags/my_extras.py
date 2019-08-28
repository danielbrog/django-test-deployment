from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all values of "arg" from the strin!
    """

    return value.replace(arg,'')
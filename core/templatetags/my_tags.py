from django import template


register = template.Library()


@register.filter
def remove_q(value, replace_to='_'):
    return value.replace('q', replace_to)


@register.simple_tag
def formula(a, b, c):
    return a+b*c


@register.inclusion_tag('test.html')
def some_inc():
    return {
        'hello': 'Hola!!!'
    }

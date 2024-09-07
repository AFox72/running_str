from django import template

register = template.Library()


@register.simple_tag()
def mediapath(link=None):
    if link:
        return f'/media/{link}'
    return '#'


@register.filter()
def mymedia(link):
    if link:
        return f'/media/{link}'
    return '#'

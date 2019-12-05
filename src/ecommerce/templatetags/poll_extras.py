from django import template

register = template.Library()

@register.filter(name='number_word')
def number_word(value, args):
    list_word = value.split()
    list_word = list_word[:args] if len(list_word) >= 50 else list_word[:len(list_word)]
    text_about = ' '.join(list_word)
    return text_about
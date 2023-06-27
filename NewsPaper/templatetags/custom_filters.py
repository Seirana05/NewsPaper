from django import template


register = template.Library()

bad_words = ['Москва', 'Москву', 'Московской', 'Москвы']

@register.filter()
def censor(some):
    text = some.split()
    for i, word in enumerate(text):
        if word in bad_words:
            text[i] = word[0] + '***'
    return ' '.join(text)
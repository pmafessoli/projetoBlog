from django import template

register = template.Library()

@register.filter(name='plural_comentarios')
def plural_comentarios(numero_comentarios):
    try:
        numero_comentarios = int(numero_comentarios)

        if numero_comentarios == 0:
            return f'Nenhum comenentário'
        elif numero_comentarios ==1:
            return  f'{numero_comentarios} comentário'
        else:
            return f'{numero_comentarios} comentários'

    except:
        return f'{numero_comentarios} comentarios(s)'
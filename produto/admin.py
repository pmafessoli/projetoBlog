from django.contrib import admin
from . import models

class VaricaoInline(admin.TabularInline):
    model = models.Varicao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VaricaoInline
    ]

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Varicao)

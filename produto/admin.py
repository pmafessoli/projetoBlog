from django.contrib import admin
from . import models

class VaricaoInline(admin.TabularInline):
    model = models.Varicao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VaricaoInline
    ]

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Varicao)

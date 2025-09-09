from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao")
    search_fields = ("nome",)
    list_filter = ("nome",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "estoque", "criado_em", "atualizado_em")
    search_fields = ("nome",)
    list_filter = ("criado_em", "atualizado_em")
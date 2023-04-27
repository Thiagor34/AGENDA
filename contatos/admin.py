from django.contrib import admin
from .models import Contatos

# Register your models here.

class AdminContatos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf', 'ativo']
    search_fields = ['nome']
    list_filter = ['ativo']
    list_display_links = ['nome']
    
    
admin.site.register(Contatos, AdminContatos)


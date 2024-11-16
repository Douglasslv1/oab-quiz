from django.contrib import admin
from .models import Funcionario, Pergunta, Resposta
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')

admin.site.register(Pergunta)
admin.site.register(Resposta)


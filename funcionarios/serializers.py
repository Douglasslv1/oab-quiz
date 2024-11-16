from rest_framework import serializers
from .models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'cpf', 'email', 'cargo', 'meta', 'data_cadastro')
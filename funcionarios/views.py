from rest_framework import generics, mixins
from .models import Funcionario
from .serializers import FuncionarioSerializer
from django.shortcuts import render
import string
from .models import Pergunta


class FuncionarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FuncionariosAPIView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class CreateFuncionarioAPIView(mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


def listar_perguntas_respostas(request):
    perguntas = Pergunta.objects.prefetch_related('respostas').all()
    letras = list(string.ascii_uppercase)  # cria uma lista de letras A, B, C, D, etc.
    return render(request, 'perguntas_respostas.html', {'perguntas': perguntas, 'letras': letras})
    #return render(request, 'perguntas_respostas.html', {'perguntas': perguntas})


    


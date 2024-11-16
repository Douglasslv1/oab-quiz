from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Funcionario
from .serializers import FuncionarioSerializer

class FuncionarioAPIView(APIView):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FuncionarioSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
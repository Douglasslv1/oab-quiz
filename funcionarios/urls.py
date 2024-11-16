from django.urls import path
from .views import CreateFuncionarioAPIView, FuncionarioAPIView, FuncionariosAPIView
from . import views

urlpatterns = [
    path('funcionario/<int:pk>', FuncionarioAPIView.as_view(), name = 'funcionario'),
    path('funcionarios/', FuncionariosAPIView.as_view(), name = 'funcionarios' ),
    path('create/', CreateFuncionarioAPIView.as_view(), name = 'create'),
    path('', views.listar_perguntas_respostas, name='listar_perguntas_respostas'),
]



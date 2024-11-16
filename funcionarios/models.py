from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50, help_text='insira o nome')
    cpf = models.CharField(max_length=11, help_text='apenas numeros', unique=True)
    email = models.EmailField()
    data_cadastro = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True 

class Funcionario(Pessoa):
    cargo = models.CharField(max_length=20)
    meta = models.BigIntegerField()
    class Meta:
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'
    def __str__(self):
        return self.cpf
    


class Pergunta(models.Model):
    texto = models.CharField(max_length=1000, help_text="Texto da pergunta")

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="respostas")
    observacao = models.TextField(help_text="Observação/resposta para a pergunta")
    resposta = models.TextField(help_text="Resposta para a pergunta", null=True, blank=True)
 
    
    def __str__(self):
        return f"Resposta para: {self.pergunta.texto}"
    


    

from django.db import models
from django.conf import settings
from django.db import models


class Empresa(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    criacao_data = models.DateTimeField(auto_now_add=True)  # Data de criação da empresa no sistema
    delecao_data = models.DateTimeField(null=True, blank=True)  # Data de deleção da empresa no sistema
    email_contato = models.EmailField(max_length=255)  # Email de contato da empresa
    telefone = models.CharField(max_length=20)  # Telefone da empresa

    def _str_(self):
        return f'{self.nome_fantasia}'

class Destino(models.Model):
    name = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    destino_url = models.URLField(max_length=200, null=True)
    descricao = models.CharField(max_length=1000)
    likes = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.likes}'
    

class List(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=255)
    Capa = models.URLField(max_length=5000, null=True)
    atracoes = models.ManyToManyField(Destino)

    def __str__(self):
        return f'{self.Nome} by {self.autor.username}'
    
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    
from django.db import models
from django.contrib.auth.models import User

class PreferenciaTipo(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Preferencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    preferencia_tipo = models.ForeignKey(PreferenciaTipo, on_delete=models.CASCADE)
    nota = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.usuario.username} - {self.preferencia_tipo.nome}: {self.nota}'

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Empresa



class Categoria(models.Model):
    name = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Destino(models.Model):
    name = models.CharField(max_length=255)
    destino_url = models.URLField(max_length=200)
    descricao = models.CharField(max_length=1000)
    coordenadas = models.CharField(max_length=100, default='(-23.4339, -45.0833)')
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    empresaid=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.name}'

    

class List(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Capa = models.URLField(max_length=5000, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now= True)
    duracao = models.IntegerField(null=True)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1000)
    comentario = models.CharField(max_length=500, null=True)
    nota = models.IntegerField(null=True)

    def _str_(self):
        return f'Roteiro by {self.autor.username}'

class Evento(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    roteiro_id = models.ForeignKey(List, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_delecao = models.DateTimeField(null = True)
    comentario = models.CharField(max_length=500, null = True)
    nota = models.FloatField(null = True)

    def _str_(self):
        return f'{self.destino_id.nome} de {self.data_inicio} a {self.data_fim}'
    
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

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


class AtracaoCaracteristica(models.Model):
    atracao = models.ForeignKey(Destino,on_delete=models.CASCADE)
    nota = models.IntegerField(default=0)
    caracteristica_tipo = models.ForeignKey(PreferenciaTipo,on_delete=models.CASCADE)

    def __str__(self):
        return self.atracao
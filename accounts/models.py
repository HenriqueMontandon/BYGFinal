from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User

class Empresa(models.Model):
    cnpj = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    empresa_groups = models.ManyToManyField(Group, verbose_name='groups', related_name='empresa_related_groups')
    empresa_user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', related_name='empresa_related_permissions')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empresa', null=True)
    
    def __str__(self):
        return self.nome_fantasia
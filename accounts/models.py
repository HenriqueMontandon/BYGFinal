from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Empresa(AbstractUser):
    cnpj = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, verbose_name='groups', related_name='empresa_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', related_name='empresa_user_permissions')

    def __str__(self):
        return self.nome_fantasia

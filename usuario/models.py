from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

from valida_cep.models import Enderecos
class Usuario(AbstractUser):
    cep = models.CharField(max_length=9, blank=True, null=True)
    endereco = models.OneToOneField(Enderecos, on_delete=models.CASCADE, blank=True, null=True)
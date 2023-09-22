
# Create your models here.
from django.db import models

class Enderecos(models.Model):
    cidade = models.CharField(max_length=100,blank=True, null=True)
    estado = models.CharField(max_length=50 ,blank=True, null=True)
    bairro = models.CharField(max_length=100 ,blank=True, null=True)
    ddd = models.CharField(max_length=2 ,blank=True, null=True)

    def __str__(self):
        return f'{self.cidade} --> {self.estado} --> {self.bairro} --> {self.ddd}'
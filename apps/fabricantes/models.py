from django.db import models

# Create your models here.



class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    pais = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.nome


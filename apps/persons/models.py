from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
from django.db import models
from vaccines.models import Vaccine
# Create your models here.

class Species(models.Model):
    vaccine = models.ManyToManyField(Vaccine, verbose_name='Vacinas', blank=True)
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=300)

    class Meta:
        verbose_name = 'Espécie'
        verbose_name_plural = 'Espécies'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
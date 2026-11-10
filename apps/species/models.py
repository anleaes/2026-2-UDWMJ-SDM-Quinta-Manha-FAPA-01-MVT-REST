from django.db import models
from vaccines.models import Vaccine
# Create your models here.

class Species(models.Model):
    vaccine = models.ManyToManyField(Vaccine, verbose_name='Vacinas', blank=True)

    class Meta:
        verbose_name = 'Espécie'
        verbose_name_plural = 'Espécies'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
from django.db import models
from vaccines.models import Vaccine
# Create your models here.

class Species(models.Model):

    class Meta:
        verbose_name = 'Espécie'
        verbose_name_plural = 'Espécies'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
from django.db import models
from batches.models import Batch

# Create your models here.

class Vaccination(models.Model):

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'
        ordering = ['id']

    def __str__(self):
        return f'Vacinação {self.id} - Lote {self.batch.number}'
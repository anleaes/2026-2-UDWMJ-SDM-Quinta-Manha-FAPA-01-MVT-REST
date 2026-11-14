from django.db import models
from batches.models import Batch

# Create your models here.

class Vaccination(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, verbose_name='Lote')
    applied_at = models.DateTimeField('Data e hora da aplicação')
    dose_number = models.IntegerField('Número da dose')
    application_site = models.CharField('Local da aplicação', max_length=100)

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'
        ordering = ['id']

    def __str__(self):
        return f'Vacinação {self.id} - Lote {self.batch.number}'
from django.db import models
from batches.models import Batch
from appointments.models import Appointment

# Create your models here.

class Vaccination(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, verbose_name='Lote')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='vaccinations', verbose_name='Atendimento')
    applied_at = models.DateTimeField('Data e hora da aplicação')
    dose_number = models.IntegerField('Número da dose')
    application_site = models.CharField('Local da aplicação', max_length=100)
    weight_kg = models.FloatField('Peso (kg)')
    notes = models.TextField('Observações', blank=True)

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'
        ordering = ['id']

    def __str__(self):
        return f'Vacinação {self.id} - Lote {self.batch.number}'
from django.db import models, transaction
from batches.models import Batch
from appointments.models import Appointment

from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone

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

    
    def apply(self):
        if self.batch.is_expired():
            raise ValidationError('Este lote está vencido.')
        with transaction.atomic():
            if not self.batch.decrease_stock():
                raise ValidationError('Este lote está sem estoque.')
            self.applied_at = timezone.now()
            self.save()

    def issue_certificate(self):
        from certificates.models import Certificate  # import aqui dentro evita import circular
        if hasattr(self, 'certificate'):
            return self.certificate
        return Certificate.objects.create(
            vaccination=self,
            number=f'CERT-{self.id:06d}',
            valid_until=date.today() + timedelta(days=self.batch.vaccine.interval_days),
        )
from django.db import models
from appointments.models import Appointment
from medications.models import Medication

# Create your models here.

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, verbose_name='Atendimento', related_name='prescriptions')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, verbose_name='Medicamento')
    dosage = models.CharField('Dosagem', max_length=50)
    frequency = models.CharField('Frequência', max_length=50)
    duration_days = models.PositiveIntegerField('Duração (dias)')
    instructions = models.TextField('Instruções', null=True, blank=True)

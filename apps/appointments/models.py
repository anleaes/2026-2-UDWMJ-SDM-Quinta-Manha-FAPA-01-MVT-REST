from django.db import models
from animals.models import Animal
from veterinarians.models import Veterinarian

# Create your models here.

class Appointment(models.Model):
    scheduled_at = models.DateTimeField('Data e hora agendada')

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'
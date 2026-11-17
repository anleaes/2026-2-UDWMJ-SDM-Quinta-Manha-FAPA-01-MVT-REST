from django.db import models
from animals.models import Animal
from veterinarians.models import Veterinarian

# Create your models here.

class Appointment(models.Model):
    scheduled_at = models.DateTimeField('Data e hora agendada')
    appointment_type = models.CharField('Tipo', max_length=20, null=True, blank=True, default='Consulta', choices=[
        ('Consulta', 'Consulta'),
        ('Vacinacao', 'Vacinacao'),
        ('Retorno', 'Retorno'),
    ])
    status = models.CharField('Status', max_length=20, null=True, blank=True, default='Agendada', choices=[
        ('Agendada', 'Agendada'),
        ('Confirmada', 'Confirmada'),
        ('Concluida', 'Concluida'),
        ('Cancelada', 'Cancelada'),
    ])
    notes = models.TextField('Observacoes', null=True, blank=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['id']

    def __str__(self):
        return f'{self.animal} - {self.scheduled_at:%d/%m/%Y %H:%M}'
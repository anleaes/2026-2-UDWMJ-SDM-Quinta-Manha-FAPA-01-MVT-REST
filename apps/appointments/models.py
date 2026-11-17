from django.db import models

# Create your models here.

class Appointment(models.Model):

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'
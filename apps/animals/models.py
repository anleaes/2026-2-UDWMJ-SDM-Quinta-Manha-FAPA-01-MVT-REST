from django.db import models
from apps.tutors.models import Tutor
from apps.species.models import Species


# Create your models here.

class Animal(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name="Tutor")
    species = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name="Espécie")
    name = models.CharField('Nome', max_length=100)
    birth_date = models.DateField('Data de Nascimento')
    sex = models.CharField('Sexo', max_length=1, choices=[('M', 'Macho'), ('F', 'Fêmea')])
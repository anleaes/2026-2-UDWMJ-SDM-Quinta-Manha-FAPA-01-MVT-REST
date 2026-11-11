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
    weight_kg = models.FloatField('Peso (kg)')
    microchip = models.CharField('Microchip', max_length=50, unique=True)
    photo = models.ImageField('Foto', upload_to='animals/', blank=True, null=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering = ['id']

    def age(self):
        from datetime import date
        today = date.today()
        if self.birth_date:
            return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return 0
    age.short_description = "Idade"
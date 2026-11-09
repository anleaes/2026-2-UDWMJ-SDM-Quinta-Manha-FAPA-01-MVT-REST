from django.db import models
from apps.persons.models import Person

# Create your models here.

class Tutor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name="Pessoa")
    photo = models.ImageField(upload_to='tutors/photos/', blank=True, null=True, verbose_name="Foto")

def __str__(self):
        return str(self.person)

class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutors"
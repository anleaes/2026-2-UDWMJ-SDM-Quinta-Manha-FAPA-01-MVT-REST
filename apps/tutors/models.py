from django.db import models
from persons.models import Person

# Create your models here.

class Tutor(Person):
    photo = models.ImageField('Foto', upload_to='tutors/photos/', blank=True, null=True)
    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'
        ordering = ['id']
    def __str__(self):
        return f'{self.name}'
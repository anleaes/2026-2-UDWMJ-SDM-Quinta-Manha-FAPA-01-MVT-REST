from django.db import models
from persons.models import Person

# Create your models here.

class Veterinarian(Person):
    crmv = models.CharField('CRMV', max_length=20, unique=True)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
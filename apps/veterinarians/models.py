from django.db import models
from persons.models import Person

# Create your models here.

class Veterinarian(Person):
    crmv = models.CharField('CRMV', max_length=20, unique=True)
    is_active = models.BooleanField('Ativo', default=True)
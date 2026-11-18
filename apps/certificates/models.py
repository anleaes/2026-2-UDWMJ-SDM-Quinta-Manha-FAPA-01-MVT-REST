from django.db import models
from vaccinations.models import Vaccination

# Create your models here.

class Certificate(models.Model):
    vaccination = models.OneToOneField(
        Vaccination,
        on_delete=models.CASCADE,
        verbose_name='Vacinação'
    )
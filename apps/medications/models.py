from django.db import models
from manufacturers.models import Manufacturer

# Create your models here.

class Medication(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Fabricante')
    name = models.CharField('Nome', max_length=100)
    active_ingredient = models.CharField('Princípio ativo', max_length=100)
    administration_route = models.CharField('Via de administração', max_length=20, choices=[
        ('Oral', 'Oral'),
        ('Injetável', 'Injetável'),
        ('Tópica', 'Tópica'),
    ])
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    is_controlled = models.BooleanField('Controlado', default=False)

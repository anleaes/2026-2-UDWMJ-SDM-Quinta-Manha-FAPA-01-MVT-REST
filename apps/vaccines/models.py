from django.db import models

from manufacturers.models import Manufacturer


class Vaccine(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, verbose_name='Fabricante'
    )
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=500)
    required_doses = models.IntegerField('Doses necessárias')
    interval_days = models.IntegerField('Intervalo entre doses (dias)')
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    is_active = models.BooleanField('Ativa', default=True)
    package_insert = models.FileField('Bula', upload_to='vaccines/package_inserts/')

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'

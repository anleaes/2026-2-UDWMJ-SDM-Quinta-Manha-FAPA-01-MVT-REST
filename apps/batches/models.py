from django.db import models

from vaccines.models import Vaccine


class Batch(models.Model):
    vaccine = models.ForeignKey(
        Vaccine, on_delete=models.CASCADE, verbose_name='Vacina'
    )
    number = models.CharField('Número', max_length=100)
    fabrication_date = models.DateField('Data de fabricação')
    expiration_date = models.DateField('Data de validade')
    quantity = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        ordering = ['id']

    def __str__(self):
        return f'{self.number}'

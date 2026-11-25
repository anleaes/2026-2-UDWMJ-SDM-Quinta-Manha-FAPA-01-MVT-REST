from django.db import models
from django.utils import timezone

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

    def is_expired(self):
        return self.expiration_date < timezone.localdate()

    def decrease_stock(self):
        if self.quantity > 0:
            self.quantity = self.quantity - 1
            self.save()
            return True
        return False

    def __str__(self):
        return f'{self.vaccine.name} - Lote {self.number}'

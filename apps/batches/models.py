from django.db import models


class Batch(models.Model):
    number = models.CharField('Número', max_length=100)
    fabrication_date = models.DateField('Data de fabricação')
    expiration_date = models.DateField('Data de validade')
    quantity = models.IntegerField('Quantidade')

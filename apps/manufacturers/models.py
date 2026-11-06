from django.db import models


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome', max_length=100, db_column='NOME')
    cnpj = models.CharField('CNPJ', max_length=14, unique=True)
    country = models.CharField('Pais', max_length=100, db_column='PAIS')
    email = models.EmailField('E-mail', max_length=254)

    class Meta:
        db_table = 'FABRICANTES_FABRICANTE'
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
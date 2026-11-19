from django.db import models

from prescriptions.models import Prescription


class Recipe(models.Model):
    prescription = models.OneToOneField(
        Prescription, on_delete=models.CASCADE, verbose_name='Prescrição'
    )
    number = models.CharField('Número', max_length=100)
    issue_date = models.DateField('Data de emissão')
    valid_until = models.DateField('Válido até')
    recipe_type = models.CharField('Tipo de receita', max_length=50)
    pdf_file = models.FileField('Arquivo PDF', upload_to='recipes/', null=True, blank=True)
    notes = models.TextField('Observações', null=True, blank=True)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['id']

    def __str__(self):
        return f'{self.number}'

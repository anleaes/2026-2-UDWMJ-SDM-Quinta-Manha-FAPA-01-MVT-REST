from django.db import models


class Recipe(models.Model):
    number = models.CharField('Número', max_length=100)
    issue_date = models.DateField('Data de emissão')
    valid_until = models.DateField('Válido até')
    recipe_type = models.CharField('Tipo de receita', max_length=50)
    pdf_file = models.FileField('Arquivo PDF', upload_to='recipes/', null=True, blank=True)
    notes = models.TextField('Observações', null=True, blank=True)

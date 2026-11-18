from django.db import models
from vaccinations.models import Vaccination

# Create your models here.

class Certificate(models.Model):
    vaccination = models.OneToOneField(
        Vaccination,
        on_delete=models.CASCADE,
        verbose_name='Vacinação'
    )
    
    number = models.CharField('Número', max_length=100, unique=True)
    issue_date = models.DateField('Data de emissão', auto_now_add=True)
    valid_until = models.DateField('Válido até')
    pdf_file = models.FileField('Arquivo PDF', upload_to='certificates/', blank=True, null=True)
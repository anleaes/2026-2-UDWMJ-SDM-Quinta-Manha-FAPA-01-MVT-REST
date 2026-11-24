from datetime import timedelta

from django.db import models
from django.utils import timezone

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

    def next_dose(self, animal):
        from vaccinations.models import Vaccination

        history = Vaccination.objects.filter(
            batch__vaccine=self, appointment__animal=animal
        ).aggregate(doses=models.Count('pk'), last_applied=models.Max('applied_at'))

        if history['doses'] == 0:
            return timezone.localdate()
        if history['doses'] >= self.required_doses:
            return None
        return timezone.localdate(history['last_applied']) + timedelta(days=self.interval_days)

    def __str__(self):
        return f'{self.name}'

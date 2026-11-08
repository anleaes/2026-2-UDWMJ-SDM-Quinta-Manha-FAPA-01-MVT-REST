from datetime import timedelta

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
        return f'{self.id} - {self.name}'

    def next_dose(self, animal):
        """Retorna a data da próxima dose, ou None sem histórico ou com doses concluídas."""
        last_application = animal.appointment_set.filter(
            vaccination__batch__vaccine=self
        ).values(
            'vaccination__applied_at', 'vaccination__dose_number'
        ).order_by(
            '-vaccination__applied_at', '-vaccination__dose_number'
        ).first()

        if last_application is None:
            return None
        if last_application['vaccination__dose_number'] >= self.required_doses:
            return None

        return last_application['vaccination__applied_at'] + timedelta(days=self.interval_days)

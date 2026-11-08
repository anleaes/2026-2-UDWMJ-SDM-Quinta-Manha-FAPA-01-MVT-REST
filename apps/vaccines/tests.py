from datetime import datetime, timedelta, timezone
from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import Mock

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from manufacturers.models import Manufacturer

from .models import Vaccine


class VaccineTests(TestCase):
    def setUp(self):
        storage_settings = override_settings(STORAGES={
            'default': {'BACKEND': 'django.core.files.storage.InMemoryStorage'},
            'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
        })
        storage_settings.enable()
        self.addCleanup(storage_settings.disable)
        self.manufacturer = Manufacturer.objects.create(
            name='Fabricante de Teste', cnpj='12345678000190',
            country='Brasil', email='teste@example.com'
        )
        self.add_url = reverse('vaccines:add_vaccine')
        self.list_url = reverse('vaccines:list_vaccines')

    def payload(self, with_file=True):
        data = {
            'manufacturer': self.manufacturer.pk,
            'name': 'Vacina & Teste',
            'description': 'Descricao para teste do cadastro.',
            'required_doses': 3,
            'interval_days': 21,
            'price': '75.50',
            'is_active': 'on',
        }
        if with_file:
            data['package_insert'] = SimpleUploadedFile(
                'bula.pdf', b'%PDF-1.4\nbula de teste',
                content_type='application/pdf'
            )
        return data

    def create_vaccine(self):
        response = self.client.post(self.add_url, self.payload())
        self.assertRedirects(response, self.list_url)
        return Vaccine.objects.get()

    def test_empty_list_and_form_with_manufacturer_and_upload(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, 'Nenhuma vacina cadastrada.')
        response = self.client.get(self.add_url)
        self.assertContains(response, 'enctype="multipart/form-data"')
        self.assertContains(response, self.manufacturer.name)
        self.assertContains(response, 'csrfmiddlewaretoken')
        for field in self.payload():
            self.assertContains(response, f'name="{field}"')
        response = self.client.get(reverse('core:home'))
        self.assertContains(
            response,
            f'<a href="{self.list_url}"><button>Vacinas</button></a>',
            html=True
        )

    def test_create_saves_manufacturer_price_and_uploaded_file(self):
        vaccine = self.create_vaccine()
        self.assertEqual(vaccine.manufacturer, self.manufacturer)
        self.assertEqual(vaccine.price, Decimal('75.50'))
        self.assertTrue(vaccine.is_active)
        with vaccine.package_insert.open('rb') as uploaded:
            self.assertEqual(uploaded.read(), b'%PDF-1.4\nbula de teste')
        response = self.client.get(self.list_url)
        self.assertContains(response, 'Vacina &amp; Teste')
        self.assertContains(response, vaccine.package_insert.url)
        for name in ('edit_vaccine', 'delete_vaccine'):
            self.assertContains(response, reverse(f'vaccines:{name}', args=[vaccine.pk]))

    def test_edit_reuses_form_and_preserves_existing_file(self):
        vaccine = self.create_vaccine()
        file_name = vaccine.package_insert.name
        url = reverse('vaccines:edit_vaccine', args=[vaccine.pk])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'vaccines/add_vaccine.html')
        self.assertEqual(response.context['form'].instance, vaccine)
        data = self.payload(with_file=False)
        data['name'] = 'Vacina Atualizada'
        data.pop('is_active')
        self.assertRedirects(self.client.post(url, data), self.list_url)
        vaccine.refresh_from_db()
        self.assertEqual(vaccine.name, 'Vacina Atualizada')
        self.assertFalse(vaccine.is_active)
        self.assertEqual(vaccine.package_insert.name, file_name)

    def test_edit_replaces_uploaded_file(self):
        vaccine = self.create_vaccine()
        data = self.payload()
        data['package_insert'] = SimpleUploadedFile(
            'bula_nova.pdf', b'%PDF-1.4\nbula atualizada',
            content_type='application/pdf'
        )
        response = self.client.post(
            reverse('vaccines:edit_vaccine', args=[vaccine.pk]), data
        )
        self.assertRedirects(response, self.list_url)
        vaccine.refresh_from_db()
        with vaccine.package_insert.open('rb') as uploaded:
            self.assertEqual(uploaded.read(), b'%PDF-1.4\nbula atualizada')

    def test_invalid_price_keeps_form_errors_and_does_not_save_file(self):
        data = self.payload()
        data['price'] = 'invalido'
        response = self.client.post(self.add_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('price', response.context['form'].errors)
        self.assertContains(response, 'errorlist')
        self.assertContains(response, 'Vacina &amp; Teste')
        self.assertFalse(Vaccine.objects.exists())
        self.assertFalse(default_storage.exists('vaccines/package_inserts/bula.pdf'))

    def test_new_vaccine_requires_file_and_existing_manufacturer(self):
        data = self.payload(with_file=False)
        data['manufacturer'] = 999999
        response = self.client.post(self.add_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('manufacturer', response.context['form'].errors)
        self.assertIn('package_insert', response.context['form'].errors)
        self.assertFalse(Vaccine.objects.exists())

    def test_delete_vaccine_keeps_manufacturer(self):
        vaccine = self.create_vaccine()
        response = self.client.get(
            reverse('vaccines:delete_vaccine', args=[vaccine.pk])
        )
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Vaccine.objects.exists())
        self.assertTrue(Manufacturer.objects.filter(pk=self.manufacturer.pk).exists())

    def test_edit_missing_vaccine_returns_404(self):
        response = self.client.get(reverse('vaccines:edit_vaccine', args=[999999]))
        self.assertEqual(response.status_code, 404)

    def test_form_post_requires_csrf_token(self):
        client = Client(enforce_csrf_checks=True)
        response = client.post(self.add_url, self.payload())
        self.assertEqual(response.status_code, 403)
        self.assertFalse(Vaccine.objects.exists())
        client.get(self.add_url)
        data = self.payload()
        data['csrfmiddlewaretoken'] = client.cookies['csrftoken'].value
        self.assertRedirects(client.post(self.add_url, data), self.list_url)


class NextDoseTests(SimpleTestCase):
    def setUp(self):
        self.vaccine = Vaccine(pk=1, required_doses=3, interval_days=21)
        self.animal = SimpleNamespace(appointment_set=Mock())
        self.applications = (
            self.animal.appointment_set.filter.return_value
            .values.return_value.order_by.return_value
        )

    def test_without_previous_application_has_no_calculated_date(self):
        self.applications.first.return_value = None
        self.assertIsNone(self.vaccine.next_dose(self.animal))

    def test_adds_configured_interval_to_last_application(self):
        applied_at = datetime(2026, 11, 8, 10, 30, tzinfo=timezone.utc)
        self.applications.first.return_value = {
            'vaccination__applied_at': applied_at,
            'vaccination__dose_number': 1,
        }
        self.assertEqual(
            self.vaccine.next_dose(self.animal),
            applied_at + timedelta(days=21)
        )

    def test_completed_doses_have_no_next_date(self):
        self.applications.first.return_value = {
            'vaccination__applied_at': datetime(2026, 11, 8, tzinfo=timezone.utc),
            'vaccination__dose_number': 3,
        }
        self.assertIsNone(self.vaccine.next_dose(self.animal))

    def test_more_doses_than_required_have_no_next_date(self):
        self.applications.first.return_value = {
            'vaccination__applied_at': datetime(2026, 11, 8, tzinfo=timezone.utc),
            'vaccination__dose_number': 4,
        }
        self.assertIsNone(self.vaccine.next_dose(self.animal))

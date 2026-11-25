from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PrescriptionForm
from .models import Prescription
from recipes.models import Recipe

# Create your views here.

def add_prescription(request):
    template_name = 'prescriptions/add_prescription.html'
    context = {}
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('prescriptions:list_prescriptions')
    form = PrescriptionForm()
    context['form'] = form
    return render(request, template_name, context)


def list_prescriptions(request):
    template_name = 'prescriptions/list_prescriptions.html'
    prescriptions = Prescription.objects.filter()
    context = {
        'prescriptions': prescriptions
    }
    return render(request, template_name, context)


def edit_prescription(request, id_prescription):
    template_name = 'prescriptions/add_prescription.html'
    context = {}
    prescription = get_object_or_404(Prescription, id=id_prescription)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescriptions:list_prescriptions')
    form = PrescriptionForm(instance=prescription)
    context['form'] = form
    return render(request, template_name, context)


def delete_prescription(request, id_prescription):
    prescription = Prescription.objects.get(id=id_prescription)
    prescription.delete()
    return redirect('prescriptions:list_prescriptions')


def issue_recipe(request, id_prescription):
    prescription = get_object_or_404(Prescription, id=id_prescription)
    if not hasattr(prescription, 'recipe'):
        if prescription.medication.is_controlled:
            recipe_type = 'Controle especial'
        else:
            recipe_type = 'Simples'
        Recipe.objects.create(
            prescription=prescription,
            number=f'REC-{prescription.id:06d}',
            valid_until=date.today() + timedelta(days=30),
            recipe_type=recipe_type
        )
    return redirect('prescriptions:list_prescriptions')

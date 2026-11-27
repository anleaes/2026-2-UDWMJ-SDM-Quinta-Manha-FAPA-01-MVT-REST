from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PrescriptionForm
from .models import Prescription
from .serializer import PrescriptionSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
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


@login_required(login_url='/contas/login/')
def list_prescriptions(request):
    template_name = 'prescriptions/list_prescriptions.html'
    prescriptions = Prescription.objects.filter()
    context = {
        'prescriptions': prescriptions
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
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


@login_required(login_url='/contas/login/')
def delete_prescription(request, id_prescription):
    prescription = Prescription.objects.get(id=id_prescription)
    prescription.delete()
    return redirect('prescriptions:list_prescriptions')


def create_recipe_for_prescription(prescription):
    if hasattr(prescription, 'recipe'):
        return prescription.recipe
    if prescription.medication.is_controlled:
        recipe_type = 'Controle especial'
    else:
        recipe_type = 'Simples'
    return Recipe.objects.create(
        prescription=prescription,
        number=f'REC-{prescription.id:06d}',
        valid_until=date.today() + timedelta(days=30),
        recipe_type=recipe_type
    )


@login_required(login_url='/contas/login/')
def issue_recipe(request, id_prescription):
    prescription = get_object_or_404(Prescription, id=id_prescription)
    create_recipe_for_prescription(prescription)
    return redirect('prescriptions:list_prescriptions')


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicationForm
from .models import Medication
from .serializer import MedicationSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_medication(request):
    template_name = 'medications/add_medication.html'
    context = {}
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('medications:list_medications')
    form = MedicationForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def list_medications(request):
    template_name = 'medications/list_medications.html'
    medications = Medication.objects.filter()
    context = {
        'medications': medications
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def edit_medication(request, id_medication):
    template_name = 'medications/add_medication.html'
    context = {}
    medication = get_object_or_404(Medication, id=id_medication)
    if request.method == 'POST':
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('medications:list_medications')
    form = MedicationForm(instance=medication)
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def delete_medication(request, id_medication):
    medication = Medication.objects.get(id=id_medication)
    medication.delete()
    return redirect('medications:list_medications')


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

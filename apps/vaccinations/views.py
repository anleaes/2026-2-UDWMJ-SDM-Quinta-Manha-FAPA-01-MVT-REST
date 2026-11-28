from django.shortcuts import render, get_object_or_404, redirect
from .forms import VaccinationForm
from .models import Vaccination
from rest_framework import viewsets, serializers
from .serializer import VaccinationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

@login_required(login_url='/contas/login/')
def add_vaccination(request):
    template_name = 'vaccinations/add_vaccination.html'
    context = {}
    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            try:
                f.apply()
                return redirect('vaccinations:list_vaccinations')
            except DjangoValidationError as e:
                form.add_error('batch', e.messages[0])
        context['form'] = form
        return render(request, template_name, context)
    context['form'] = VaccinationForm()
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def list_vaccinations(request):
    template_name = 'vaccinations/list_vaccinations.html'
    vaccinations = Vaccination.objects.filter()
    context = {
        'vaccinations': vaccinations
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def edit_vaccination(request, id_vaccination):
    template_name = 'vaccinations/add_vaccination.html'
    context = {}
    vaccination = get_object_or_404(Vaccination, id=id_vaccination)
    if request.method == 'POST':
        form = VaccinationForm(request.POST, instance=vaccination)
        if form.is_valid():
            form.save()
            return redirect('vaccinations:list_vaccinations')
    form = VaccinationForm(instance=vaccination)
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def delete_vaccination(request, id_vaccination):
    vaccination = Vaccination.objects.get(id=id_vaccination)
    vaccination.delete()
    return redirect('vaccinations:list_vaccinations')


@login_required(login_url='/contas/login/')
def issue_certificate(request, id_vaccination):
    vaccination = get_object_or_404(Vaccination, id=id_vaccination)
    vaccination.issue_certificate()
    return redirect('vaccinations:list_vaccinations')


class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

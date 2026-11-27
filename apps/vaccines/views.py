from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import VaccineForm
from .models import Vaccine
from .serializer import VaccineSerializer


@login_required(login_url='/contas/login/')
def add_vaccine(request):
    template_name = 'vaccines/add_vaccine.html'
    context = {}
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('vaccines:list_vaccines')
    form = VaccineForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def list_vaccines(request):
    template_name = 'vaccines/list_vaccines.html'
    vaccines = Vaccine.objects.filter()
    context = {
        'vaccines': vaccines
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def edit_vaccine(request, id_vaccine):
    template_name = 'vaccines/add_vaccine.html'
    context = {}
    vaccine = get_object_or_404(Vaccine, id=id_vaccine)
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES, instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect('vaccines:list_vaccines')
    form = VaccineForm(instance=vaccine)
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def delete_vaccine(request, id_vaccine):
    vaccine = Vaccine.objects.get(id=id_vaccine)
    vaccine.delete()
    return redirect('vaccines:list_vaccines')


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

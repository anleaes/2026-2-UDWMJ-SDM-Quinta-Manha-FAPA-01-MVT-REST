from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppointmentForm
from .models import Appointment
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import AppointmentSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_appointment(request):
    template_name = 'appointments/add_appointment.html'
    context = {}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('appointments:list_appointments')
    form = AppointmentForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def list_appointments(request):
    template_name = 'appointments/list_appointments.html'
    appointments = Appointment.objects.filter()#Appointment.objects.prefetch_related('vaccinations')
    context = {
        'appointments': appointments
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def edit_appointment(request, id_appointment):
    template_name = 'appointments/add_appointment.html'
    context = {}
    appointment = get_object_or_404(Appointment, id=id_appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments:list_appointments')
    form = AppointmentForm(instance=appointment)
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def delete_appointment(request, id_appointment):
    appointment = Appointment.objects.get(id=id_appointment)
    appointment.delete()
    return redirect('appointments:list_appointments')


@login_required(login_url='/contas/login/')
def confirm_appointment(request, id_appointment):
    appointment = get_object_or_404(Appointment, id=id_appointment)
    appointment.confirm()
    return redirect('appointments:list_appointments')


@login_required(login_url='/contas/login/')
def complete_appointment(request, id_appointment):
    appointment = get_object_or_404(Appointment, id=id_appointment)
    appointment.complete()
    return redirect('appointments:list_appointments')


@login_required(login_url='/contas/login/')
def cancel_appointment(request, id_appointment):
    appointment = get_object_or_404(Appointment, id=id_appointment)
    appointment.cancel()
    return redirect('appointments:list_appointments')


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
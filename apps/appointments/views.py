from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppointmentForm
from .models import Appointment

# Create your views here.

def add_appointment(request):
    template_name = 'appointments/add_appointment.html'
    context = {}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('appointments:list_appointments')
    form = AppointmentForm()
    context['form'] = form
    return render(request, template_name, context)


def list_appointments(request):
    template_name = 'appointments/list_appointments.html'
    appointments = appointments = Appointment.objects.filter()#Appointment.objects.prefetch_related('vaccinations')
    context = {
        'appointments': appointments
    }
    return render(request, template_name, context)


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


def delete_appointment(request, id_appointment):
    appointment = Appointment.objects.get(id=id_appointment)
    appointment.delete()
    return redirect('appointments:list_appointments')


def confirm_appointment(request, id_appointment):
    appointment = get_object_or_404(Appointment, id=id_appointment)
    if appointment.status != 'Confirmada':
        appointment.status = 'Confirmada'
        appointment.save()
    return redirect('appointments:list_appointments')


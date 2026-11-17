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

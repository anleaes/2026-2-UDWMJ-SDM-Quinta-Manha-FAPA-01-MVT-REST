from django.shortcuts import render, get_object_or_404, redirect
from .forms import PrescriptionForm
from .models import Prescription

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

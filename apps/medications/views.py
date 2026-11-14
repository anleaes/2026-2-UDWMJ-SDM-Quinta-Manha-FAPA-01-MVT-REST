from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicationForm
from .models import Medication

# Create your views here.

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

from django.shortcuts import render, get_object_or_404, redirect
from .forms import VaccinationForm
from .models import Vaccination

# Create your views here.

def add_vaccination(request):
    template_name = 'vaccinations/add_vaccination.html'
    context = {}
    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('vaccinations:list_vaccinations')
    form = VaccinationForm()
    context['form'] = form
    return render(request, template_name, context)


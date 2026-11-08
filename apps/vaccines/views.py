from django.shortcuts import render, redirect, get_object_or_404

from .forms import VaccineForm
from .models import Vaccine


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
    else:
        form = VaccineForm()
    context['form'] = form
    return render(request, template_name, context)

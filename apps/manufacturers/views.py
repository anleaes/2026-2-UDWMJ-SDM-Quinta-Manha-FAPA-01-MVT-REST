from django.shortcuts import render, redirect, get_object_or_404

from .forms import ManufacturerForm
from .models import Manufacturer


# Create your views here.


def add_manufacturer(request):
    template_name = 'manufacturers/add_manufacturer.html'
    context = {}
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('manufacturers:list_manufacturers')
    else:
        form = ManufacturerForm()

    context['form'] = form
    return render(request, template_name, context)

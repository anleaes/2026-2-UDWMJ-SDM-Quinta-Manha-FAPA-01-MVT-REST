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

def list_manufacturers(request):
    template_name = 'manufacturers/list_manufacturers.html'
    manufacturers = Manufacturer.objects.filter()

    context = {
        'manufacturers': manufacturers
    }
    return render(request, template_name, context)

def edit_manufacturer(request, pk):
    template_name = 'manufacturers/add_manufacturer.html'
    context = {}
    manufacturer = get_object_or_404(Manufacturer, pk=pk)

    if request.method == 'POST':
        form = ManufacturerForm(request.POST, instance=manufacturer)

        if form.is_valid():
            form.save()
            return redirect('manufacturers:list_manufacturers')
    else:
        form = ManufacturerForm(instance=manufacturer)

    context['form'] = form
    return render(request, template_name, context)


def delete_manufacturer(request, pk):
    manufacturer = Manufacturer.objects.get(id=pk)
    manufacturer.delete()
    return redirect('manufacturers:list_manufacturers')

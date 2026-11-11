from django.shortcuts import render, get_object_or_404, redirect
from .forms import VeterinarianForm
from .models import Veterinarian

# Create your views here.

def add_veterinarian(request):
    template_name = 'veterinarians/add_veterinarian.html'
    context = {}
    if request.method == 'POST':
        form = VeterinarianForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('veterinarians:list_veterinarians')
    form = VeterinarianForm()
    context['form'] = form
    return render(request, template_name, context)


def list_veterinarians(request):
    template_name = 'veterinarians/list_veterinarians.html'
    veterinarians = Veterinarian.objects.filter()
    context = {
        'veterinarians': veterinarians
    }
    return render(request, template_name, context)


def edit_veterinarian(request, id_veterinarian):
    template_name = 'veterinarians/add_veterinarian.html'
    context = {}
    veterinarian = get_object_or_404(Veterinarian, id=id_veterinarian)
    if request.method == 'POST':
        form = VeterinarianForm(request.POST, instance=veterinarian)
        if form.is_valid():
            form.save()
            return redirect('veterinarians:list_veterinarians')
    form = VeterinarianForm(instance=veterinarian)
    context['form'] = form
    return render(request, template_name, context)


def delete_veterinarian(request, id_veterinarian):
    veterinarian = Veterinarian.objects.get(id=id_veterinarian)
    veterinarian.delete()
    return redirect('veterinarians:list_veterinarians')
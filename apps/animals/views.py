from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnimalForm
from .models import Animal

# Create your views here.

def animal_list(request):
    template_name = 'animals/list_animals.html'
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, template_name, context)

def animal_create(request):
    template_name = 'animals/add_animal.html'
    context = {}
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animals:animal_list')
    form = AnimalForm()
    context['form'] = form
    return render(request, template_name, context)

def animal_update(request, pk):
    template_name = 'animals/add_animal.html'
    context = {}
    animal = get_object_or_404(Animal, id=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animals:animal_list')
    form = AnimalForm(instance=animal)
    context['form'] = form
    return render(request, template_name, context)

def animal_delete(request, pk):
    animal = get_object_or_404(Animal, id=pk)
    animal.delete()
    return redirect('animals:animal_list')
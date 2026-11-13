from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnimalForm
from .models import Animal

# Create your views here.# Create your views here.

def list_animals(request):
    template_name = 'animals/list_animals.html'
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, template_name, context)

def add_animal(request):
    template_name = 'animals/add_animal.html'
    context = {}
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('animals:list_animals')
    form = AnimalForm()
    context['form'] = form
    return render(request, template_name, context)

def edit_animal(request, id_animal):
    template_name = 'animals/add_animal.html'
    context = {}
    animal = get_object_or_404(Animal, id=id_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('animals:list_animals')
    form = AnimalForm(instance=animal)
    context['form'] = form
    return render(request, template_name, context)

def delete_animal(request, id_animal):
    animal = Animal.objects.get(id=id_animal)
    animal.delete()
    return redirect('animals:list_animals')

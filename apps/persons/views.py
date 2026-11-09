from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PersonForm
from .models import Person

# Create your views here.

def add_person(request):
    template_name = 'persons/add_person.html'
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persons:list_persons')
    else:
        form = PersonForm()
    return render(request, template_name, {'form': form})

def list_persons(request):
    template_name = 'persons/list_persons.html'
    persons = Person.objects.filter()
    return render(request, template_name, {'persons': persons})

def edit_person(request, id_person):
    template_name = 'persons/add_person.html'
    person = get_object_or_404(Person, id=id_person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('persons:list_persons')
    else:
        form = PersonForm(instance=person)
    return render(request, template_name, {'form': form})
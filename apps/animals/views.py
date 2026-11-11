from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnimalForm
from .models import Animal

# Create your views here.

def animal_list(request):
    template_name = 'animals/animal_list.html'
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, template_name, context)
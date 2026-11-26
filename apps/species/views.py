from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpeciesForm
from .models import Species
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import SpeciesSerializer
# Create your views here.

def add_species(request):
    template_name = 'species/add_species.html'
    if request.method == 'POST':
        form = SpeciesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('species:list_species')
    else:
        form = SpeciesForm()
    return render(request, template_name, {'form': form})

def list_species(request):
    template_name = 'species/list_species.html'
    species = Species.objects.filter()
    return render(request, template_name, {'species': species})

def edit_species(request, id_species):
    template_name = 'species/add_species.html'
    species = get_object_or_404(Species, id=id_species)
    if request.method == 'POST':
        form = SpeciesForm(request.POST, instance=species)
        if form.is_valid():
            form.save()
            return redirect('species:list_species')
    else:
        form = SpeciesForm(instance=species)
    return render(request, template_name, {'form': form})

def delete_species(request, id_species):
    species = get_object_or_404(Species, id=id_species)
    species.delete()
    return redirect('species:list_species')


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpeciesForm
from .models import Species
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

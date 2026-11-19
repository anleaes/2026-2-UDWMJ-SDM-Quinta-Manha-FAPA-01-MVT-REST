from django.shortcuts import render, redirect, get_object_or_404

from .forms import RecipeForm
from .models import Recipe


def add_recipe(request):
    template_name = 'recipes/add_recipe.html'
    context = {}
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('recipes:list_recipes')
    form = RecipeForm()
    context['form'] = form
    return render(request, template_name, context)

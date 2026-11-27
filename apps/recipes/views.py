from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import RecipeForm
from .models import Recipe
from .serializer import RecipeSerializer


@login_required(login_url='/contas/login/')
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


@login_required(login_url='/contas/login/')
def list_recipes(request):
    template_name = 'recipes/list_recipes.html'
    recipes = Recipe.objects.filter()
    context = {
        'recipes': recipes
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def edit_recipe(request, id_recipe):
    template_name = 'recipes/add_recipe.html'
    context = {}
    recipe = get_object_or_404(Recipe, id=id_recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:list_recipes')
    form = RecipeForm(instance=recipe)
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def delete_recipe(request, id_recipe):
    recipe = Recipe.objects.get(id=id_recipe)
    recipe.delete()
    return redirect('recipes:list_recipes')


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

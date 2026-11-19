from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('adicionar/', views.add_recipe, name='add_recipe'),
    path('listar/', views.list_recipes, name='list_recipes'),
]

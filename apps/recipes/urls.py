from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'recipes'

router = routers.SimpleRouter()
router.register('', views.RecipeViewSet, basename='receitas')

urlpatterns = [
    path('adicionar/', views.add_recipe, name='add_recipe'),
    path('listar/', views.list_recipes, name='list_recipes'),
    path('editar/<int:id_recipe>/', views.edit_recipe, name='edit_recipe'),
    path('excluir/<int:id_recipe>/', views.delete_recipe, name='delete_recipe'),
    path('', include(router.urls)),
]

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'species'

router = routers.SimpleRouter()
router.register('', views.SpeciesViewSet, basename='especies')

urlpatterns = [
    path('listar/', views.list_species, name='list_species'),
    path('adicionar/', views.add_species, name='add_species'),
    path('editar/<int:id_species>/', views.edit_species, name='edit_species'),
    path('excluir/<int:id_species>/', views.delete_species, name='delete_species'),
    path('', include(router.urls)),
]
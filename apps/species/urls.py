from django.urls import path
from . import views

app_name = 'species'

urlpatterns = [
    path('listar/', views.list_species, name='list_species'),
    path('adicionar/', views.add_species, name='add_species'),
    path('editar/<int:id_species>/', views.edit_species, name='edit_species'),
]
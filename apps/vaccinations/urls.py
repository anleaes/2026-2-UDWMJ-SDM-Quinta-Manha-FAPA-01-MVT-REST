from django.urls import path
from . import views

app_name = 'vaccinations'

urlpatterns = [
    path('listar/', views.list_vaccinations, name='list_vaccinations'),
    path('adicionar/', views.add_vaccination, name='add_vaccination'),
    path('editar/<int:id_vaccination>/', views.edit_vaccination, name='edit_vaccination'),
    path('excluir/<int:id_vaccination>/', views.delete_vaccination, name='delete_vaccination'),
]
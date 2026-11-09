from django.urls import path
from . import views

app_name = 'veterinarians'

urlpatterns = [
    path('adicionar/', views.add_veterinarian, name='add_veterinarian'),
    path('listar/', views.list_veterinarians, name='list_veterinarians'),
    path('editar/<int:id_veterinarian>/', views.edit_veterinarian, name='edit_veterinarian'),
    path('excluir/<int:id_veterinarian>/', views.delete_veterinarian, name='delete_veterinarian'),
]
from django.urls import path
from . import views

app_name = 'veterinarians'

urlpatterns = [
    path('adicionar/', views.add_veterinarian, name='add_veterinarian'),
    path('listar/', views.list_veterinarians, name='list_veterinarians'),
]
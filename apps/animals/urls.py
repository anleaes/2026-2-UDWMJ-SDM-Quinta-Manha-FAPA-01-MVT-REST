from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('listar/', views.list_animals, name='list_animals'),
    path('adicionar/', views.add_animal, name='add_animal'),
    path('editar/<int:id_animal>/', views.edit_animal, name='edit_animal'),
    path('excluir/<int:id_animal>/', views.delete_animal, name='delete_animal'),
]
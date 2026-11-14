from django.urls import path
from . import views

app_name = 'medications'

urlpatterns = [
    path('adicionar/', views.add_medication, name='add_medication'),
    path('listar/', views.list_medications, name='list_medications'),
    path('editar/<int:id_medication>/', views.edit_medication, name='edit_medication'),
]

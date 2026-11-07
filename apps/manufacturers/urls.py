from django.urls import path
from . import views

app_name = 'manufacturers'

urlpatterns = [
    path('adicionar/', views.add_manufacturer, name='add_manufacturer'),
    path('listar/', views.list_manufacturers, name='list_manufacturers'),
    path('editar/<int:pk>/', views.edit_manufacturer, name='edit_manufacturer'),
    path('excluir/<int:pk>/', views.delete_manufacturer, name='delete_manufacturer'),
]

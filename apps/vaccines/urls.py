from django.urls import path
from . import views

app_name = 'vaccines'

urlpatterns = [
    path('adicionar/', views.add_vaccine, name='add_vaccine'),
    path('listar/', views.list_vaccines, name='list_vaccines'),
    path('editar/<int:id_vaccine>/', views.edit_vaccine, name='edit_vaccine'),
]

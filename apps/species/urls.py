from django.urls import path
from . import views

app_name = 'species'

urlpatterns = [
    path('listar/', views.list_species, name='list_species'),
]
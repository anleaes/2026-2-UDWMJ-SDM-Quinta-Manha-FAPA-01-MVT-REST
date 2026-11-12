from django.urls import path
from . import views

app_name = 'vaccinations'

urlpatterns = [
    path('listar/', views.list_vaccinations, name='list_vaccinations'),
    path('adicionar/', views.add_vaccination, name='add_vaccination'),
]
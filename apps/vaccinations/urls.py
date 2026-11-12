from django.urls import path
from . import views

app_name = 'vaccinations'

urlpatterns = [
    path('listar/', views.list_vaccinations, name='list_vaccinations'),
]
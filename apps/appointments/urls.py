from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('listar/', views.list_appointments, name='list_appointments'),
    path('adicionar/', views.add_appointment, name='add_appointment'),
]
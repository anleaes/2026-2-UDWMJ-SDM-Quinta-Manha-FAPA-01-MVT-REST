from django.urls import path
from . import views

app_name = 'prescriptions'

urlpatterns = [
    path('adicionar/', views.add_prescription, name='add_prescription'),
]

from django.urls import path
from . import views

app_name = 'medications'

urlpatterns = [
    path('adicionar/', views.add_medication, name='add_medication'),
]

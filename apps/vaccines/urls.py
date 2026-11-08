from django.urls import path
from . import views

app_name = 'vaccines'

urlpatterns = [
    path('adicionar/', views.add_vaccine, name='add_vaccine'),
]

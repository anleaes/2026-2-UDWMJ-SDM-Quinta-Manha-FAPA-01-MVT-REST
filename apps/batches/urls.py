from django.urls import path
from . import views

app_name = 'batches'

urlpatterns = [
    path('adicionar/', views.add_batch, name='add_batch'),
    path('listar/', views.list_batches, name='list_batches'),
]

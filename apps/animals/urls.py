from django.urls import path
from . import views

app_name = 'animals'
urlpatterns = [path('listar/', views.animal_list, name='animal_list')]
urlpatterns = [
    path('listar/', views.animal_list, name='animal_list'),
    path('adicionar/', views.animal_create, name='animal_create'),
]
urlpatterns = [
    path('listar/', views.animal_list, name='animal_list'),
    path('adicionar/', views.animal_create, name='animal_create'),
    path('editar/<int:pk>/', views.animal_update, name='animal_update'),
]
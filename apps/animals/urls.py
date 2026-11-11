from django.urls import path
from . import views

app_name = 'animals'
urlpatterns = [path('listar/', views.animal_list, name='animal_list')]
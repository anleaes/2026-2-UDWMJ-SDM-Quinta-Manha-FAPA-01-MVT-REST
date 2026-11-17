from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('listar/', views.list_appointments, name='list_appointments'),
    path('adicionar/', views.add_appointment, name='add_appointment'),
    path('editar/<int:id_appointment>/', views.edit_appointment, name='edit_appointment'),
    path('excluir/<int:id_appointment>/', views.delete_appointment, name='delete_appointment'),
    path('confirmar/<int:id_appointment>/', views.confirm_appointment, name='confirm_appointment'),
    path('concluir/<int:id_appointment>/', views.complete_appointment, name='complete_appointment'),
]
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'veterinarians'

router = routers.SimpleRouter()
router.register('', views.VeterinarianViewSet, basename='veterinarios')

urlpatterns = [
    path('adicionar/', views.add_veterinarian, name='add_veterinarian'),
    path('listar/', views.list_veterinarians, name='list_veterinarians'),
    path('editar/<int:id_veterinarian>/', views.edit_veterinarian, name='edit_veterinarian'),
    path('excluir/<int:id_veterinarian>/', views.delete_veterinarian, name='delete_veterinarian'),
    path('', include(router.urls)),
]

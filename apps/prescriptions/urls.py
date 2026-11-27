from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'prescriptions'

router = routers.SimpleRouter()
router.register('', views.PrescriptionViewSet, basename='prescricoes')

urlpatterns = [
    path('adicionar/', views.add_prescription, name='add_prescription'),
    path('listar/', views.list_prescriptions, name='list_prescriptions'),
    path('editar/<int:id_prescription>/', views.edit_prescription, name='edit_prescription'),
    path('excluir/<int:id_prescription>/', views.delete_prescription, name='delete_prescription'),
    path('emitir-receita/<int:id_prescription>/', views.issue_recipe, name='issue_recipe'),
    path('', include(router.urls)),
]

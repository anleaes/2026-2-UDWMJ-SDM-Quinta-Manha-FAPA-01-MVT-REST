from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'medications'

router = routers.SimpleRouter()
router.register('', views.MedicationViewSet, basename='medicamentos')

urlpatterns = [
    path('adicionar/', views.add_medication, name='add_medication'),
    path('listar/', views.list_medications, name='list_medications'),
    path('editar/<int:id_medication>/', views.edit_medication, name='edit_medication'),
    path('excluir/<int:id_medication>/', views.delete_medication, name='delete_medication'),
    path('', include(router.urls)),
]

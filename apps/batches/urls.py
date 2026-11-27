from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'batches'

router = routers.SimpleRouter()
router.register('', views.BatchViewSet, basename='lotes')

urlpatterns = [
    path('adicionar/', views.add_batch, name='add_batch'),
    path('listar/', views.list_batches, name='list_batches'),
    path('editar/<int:id_batch>/', views.edit_batch, name='edit_batch'),
    path('excluir/<int:id_batch>/', views.delete_batch, name='delete_batch'),
    path('', include(router.urls)),
]

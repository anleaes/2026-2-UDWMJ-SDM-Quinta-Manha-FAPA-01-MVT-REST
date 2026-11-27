from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'manufacturers'

router = routers.SimpleRouter()
router.register('', views.ManufacturerViewSet, basename='fabricantes')

urlpatterns = [
    path('adicionar/', views.add_manufacturer, name='add_manufacturer'),
    path('listar/', views.list_manufacturers, name='list_manufacturers'),
    path('editar/<int:id_manufacturer>/', views.edit_manufacturer, name='edit_manufacturer'),
    path('excluir/<int:id_manufacturer>/', views.delete_manufacturer, name='delete_manufacturer'),
    path('', include(router.urls)),
]

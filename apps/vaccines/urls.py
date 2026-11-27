from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'vaccines'

router = routers.SimpleRouter()
router.register('', views.VaccineViewSet, basename='vacinas')

urlpatterns = [
    path('adicionar/', views.add_vaccine, name='add_vaccine'),
    path('listar/', views.list_vaccines, name='list_vaccines'),
    path('editar/<int:id_vaccine>/', views.edit_vaccine, name='edit_vaccine'),
    path('excluir/<int:id_vaccine>/', views.delete_vaccine, name='delete_vaccine'),
    path('', include(router.urls)),
]

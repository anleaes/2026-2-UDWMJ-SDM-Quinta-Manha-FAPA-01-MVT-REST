from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'persons'

router = routers.SimpleRouter()
router.register('', views.PersonViewSet, basename='pessoas')

urlpatterns = [
    path('listar/', views.list_persons, name='list_persons'),
    path('adicionar/', views.add_person, name='add_person'),
    path('editar/<int:id_person>/', views.edit_person, name='edit_person'),
    path('excluir/<int:id_person>/', views.delete_person, name='delete_person'),
    path('', include(router.urls)),
]

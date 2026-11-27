from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'tutors'

router = routers.SimpleRouter()
router.register('', views.TutorViewSet, basename='tutores')

urlpatterns = [
    path('adicionar/', views.add_tutor, name='add_tutor'),
    path('listar/', views.list_tutors, name='list_tutors'),
    path('editar/<int:id_tutor>/', views.edit_tutor, name='edit_tutor'),
    path('excluir/<int:id_tutor>/', views.delete_tutor, name='delete_tutor'),
    path('', include(router.urls)),
]
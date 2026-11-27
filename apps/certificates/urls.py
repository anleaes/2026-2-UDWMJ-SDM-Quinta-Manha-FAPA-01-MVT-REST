from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'certificates'

router = routers.SimpleRouter()
router.register('', views.CertificateViewSet, basename='certificates')

urlpatterns = [
    path('listar/', views.list_certificates, name='list_certificates'),
    path('adicionar/', views.add_certificate, name='add_certificate'),
    path('editar/<int:id_certificate>/', views.edit_certificate, name='edit_certificate'),
    path('excluir/<int:id_certificate>/', views.delete_certificate, name='delete_certificate'),
    path('', include(router.urls)),
]
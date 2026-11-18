from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('listar/', views.list_certificates, name='list_certificates'),
]
from django.urls import path
from apps.tutors.views import TutorCreateView, TutorDeleteView, TutorListView, TutorUpdateView

app_name = 'tutors'

urlpatterns = [
    path('', TutorListView.as_view(), name='tutor_list'),
    path('novo/', TutorCreateView.as_view(), name='tutor_create'),
    path('<int:pk>/editar/', TutorUpdateView.as_view(), name='tutor_update'),
    path('<int:pk>/excluir/', TutorDeleteView.as_view(), name='tutor_delete'),
]
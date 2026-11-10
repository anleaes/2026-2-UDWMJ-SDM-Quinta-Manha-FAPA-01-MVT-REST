from django.urls import path
from apps.tutors.views import TutorCreateView, TutorListView

app_name = 'tutors'

urlpatterns = [
    path('', TutorListView.as_view(), name='tutor_list'),
    path('novo/', TutorCreateView.as_view(), name='tutor_create'),
]
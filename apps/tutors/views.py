from django.urls import reverse_lazy
from django.views.generic import  DeleteView, ListView, CreateView, UpdateView
from .models import Tutor
from .forms import TutorForm

# Create your views here.

class TutorListView(ListView):
    model = Tutor
    template_name = 'tutors/list_tutor.html'
    context_object_name = 'tutors'

class TutorCreateView(CreateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'tutors/add_tutor.html'
    success_url = reverse_lazy('tutors:tutor_list')

class TutorUpdateView(UpdateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'tutors/add_tutor.html'
    success_url = reverse_lazy('tutors:tutor_list')

class TutorDeleteView(DeleteView):
    model = Tutor
    template_name = 'tutors/delete_tutor.html'
    success_url = reverse_lazy('tutors:tutor_list')
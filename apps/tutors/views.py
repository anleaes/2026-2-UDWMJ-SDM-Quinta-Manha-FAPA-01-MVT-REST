from django.urls import reverse_lazy
from django.views.generic import  ListView, CreateView
from .models import Tutor
from .forms import TutorForm

# Create your views here.

class TutorListView(ListView):
    model = Tutor
    template_name = 'tutors/tutor_list.html'
    context_object_name = 'tutors'

class TutorCreateView(CreateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'tutors/tutor_form.html'
    success_url = reverse_lazy('tutors:tutor_list')
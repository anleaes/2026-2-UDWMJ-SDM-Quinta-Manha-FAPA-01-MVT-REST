from django.shortcuts import render, get_object_or_404, redirect
from .forms import TutorForm
from .models import Tutor

# Create your views here.

def add_tutor(request):
    template_name = 'tutors/add_tutor.html'
    context = {}
    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tutors:list_tutors')
    form = TutorForm()
    context['form'] = form
    return render(request, template_name, context)
def list_tutors(request):
    template_name = 'tutors/list_tutors.html'
    tutors = Tutor.objects.filter()
    context = {
        'tutors': tutors
    }
    return render(request, template_name, context)
def edit_tutor(request, id_tutor):
    template_name = 'tutors/add_tutor.html'
    context = {}
    tutor = get_object_or_404(Tutor, id=id_tutor)
    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutors:list_tutors')
    form = TutorForm(instance=tutor)
    context['form'] = form
    return render(request, template_name, context)
def delete_tutor(request, id_tutor):
    tutor = Tutor.objects.get(id=id_tutor)
    tutor.delete()
    return redirect('tutors:list_tutors')
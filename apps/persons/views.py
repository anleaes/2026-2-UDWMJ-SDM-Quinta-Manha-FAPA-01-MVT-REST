from django.shortcuts import render, get_object_or_404, redirect
from .forms import PersonForm
from .models import Person
from .serializer import PersonSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_person(request):
    template_name = 'persons/add_person.html'
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persons:list_persons')
    else:
        form = PersonForm()
    return render(request, template_name, {'form': form})


@login_required(login_url='/contas/login/')
def list_persons(request):
    template_name = 'persons/list_persons.html'
    persons = Person.objects.filter()
    return render(request, template_name, {'persons': persons})


@login_required(login_url='/contas/login/')
def edit_person(request, id_person):
    template_name = 'persons/add_person.html'
    person = get_object_or_404(Person, id=id_person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('persons:list_persons')
    else:
        form = PersonForm(instance=person)
    return render(request, template_name, {'form': form})


@login_required(login_url='/contas/login/')
def delete_person(request, id_person):
    person = get_object_or_404(Person, id=id_person)
    person.delete()
    return redirect('persons:list_persons')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
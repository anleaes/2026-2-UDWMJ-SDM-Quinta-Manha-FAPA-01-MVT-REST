from django.shortcuts import render, get_object_or_404, redirect
from .forms import CertificateForm
from .models import Certificate

# Create your views here.

def list_certificates(request):
    template_name = 'certificates/list_certificates.html'
    certificates = Certificate.objects.all()
    context = {'certificates': certificates}
    return render(request, template_name, context)

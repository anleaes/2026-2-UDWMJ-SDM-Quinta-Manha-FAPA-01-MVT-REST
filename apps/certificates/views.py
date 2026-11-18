from django.shortcuts import render, get_object_or_404, redirect
from .forms import CertificateForm
from .models import Certificate

# Create your views here.

def list_certificates(request):
    template_name = 'certificates/list_certificates.html'
    certificates = Certificate.objects.all()
    context = {'certificates': certificates}
    return render(request, template_name, context)

def add_certificate(request):
    template_name = 'certificates/add_certificate.html'
    context = {}
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('certificates:list_certificates')
    form = CertificateForm()
    context['form'] = form
    return render(request, template_name, context)
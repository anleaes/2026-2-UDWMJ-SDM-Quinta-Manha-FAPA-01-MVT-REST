from django.shortcuts import render, redirect, get_object_or_404

from .forms import BatchForm
from .models import Batch


def add_batch(request):
    template_name = 'batches/add_batch.html'
    context = {}
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('batches:list_batches')
    else:
        form = BatchForm()
    context['form'] = form
    return render(request, template_name, context)

from django import forms
from .models import Vaccination

class VaccinationForm(forms.ModelForm):

    class Meta:
        model = Vaccination
        exclude = ()
        
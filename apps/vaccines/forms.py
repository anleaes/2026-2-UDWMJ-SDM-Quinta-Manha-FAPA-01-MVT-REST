from django import forms

from animals.models import Animal

from .models import Vaccine


class VaccineForm(forms.ModelForm):

    class Meta:
        model = Vaccine
        exclude = ()



class VaccineNextDoseForm(forms.Form):
    animal = forms.ModelChoiceField(label='Animal', queryset=Animal.objects.all())

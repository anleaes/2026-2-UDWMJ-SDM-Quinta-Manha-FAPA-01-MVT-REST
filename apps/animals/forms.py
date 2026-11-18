from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ()
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
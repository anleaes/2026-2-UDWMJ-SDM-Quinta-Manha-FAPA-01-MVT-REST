from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        exclude = ()
        widgets = {
            'valid_until': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
# apps/passengers/forms.py
from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'document', 'email', 'phone', 'date_birth', 'document_type']
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre',
            }),
            'document': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el telefono',
            }),
            'document_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el tipo de documento',
            }),

        }
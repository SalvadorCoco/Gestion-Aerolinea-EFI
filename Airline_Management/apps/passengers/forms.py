# apps/passengers/forms.py
from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'}),
        }
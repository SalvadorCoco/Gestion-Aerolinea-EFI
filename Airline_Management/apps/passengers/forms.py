# apps/passengers/forms.py
from django import forms
from .models import Passenger # Asegúrate que importas 'Passenger' del modelo

class PassengerForm(forms.ModelForm): # <-- Cambia esto a 'PassengerForm' si no lo está
    class Meta:
        model = Passenger # <-- Asegúrate que sea 'Passenger'
        fields = '__all__' # O la lista de campos que quieras
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'}), # Ajusta el nombre del campo si es necesario (date_birth vs fechaNacimiento)
        }
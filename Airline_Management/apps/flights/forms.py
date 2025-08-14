from django import forms
from apps.flights.models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        # Saco departure_date porque es no editable en models (auto_now_add=True)
        exclude = ['departure_date']
        widgets = {
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Origen'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destino'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'arrival_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Duración (HH:MM:SS)'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'base_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio base'}),
        }

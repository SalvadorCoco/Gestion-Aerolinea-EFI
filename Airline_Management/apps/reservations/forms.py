from django import forms
from apps.reservations.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['passenger_id', 'seating_id', 'price']
        widgets = {
            'passenger_id' : forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'seating_id' : forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'price' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Numero de filas'
                }
            ),
        } 

from django import forms
from apps.flights.models import Flight
from apps.passengers.models import Passenger
from apps.airplanes.models import Seating
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['flight_id', 'passenger_id', 'seating_id', 'price']

    # Filtro para mostrar solo asientos disponibles
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seating_id'].queryset = Seating.objects.filter(state=False)

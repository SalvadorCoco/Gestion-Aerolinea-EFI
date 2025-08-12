from django import forms
from apps.flights.models import Flight
from apps.passengers.models import Passenger
from apps.airplanes.models import Seating
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['flight_id', 'passenger_id', 'seating_id', 'price']

    def __init__(self, *args, **kwargs):
        airplane = kwargs.pop('airplane', None)  # Sacamos airplane para que no moleste
        super().__init__(*args, **kwargs)

        # Filtramos asientos disponibles
        qs = Seating.objects.filter(state=False)
        if airplane:
            qs = qs.filter(airplane_id=airplane)

        self.fields['seating_id'].queryset = qs


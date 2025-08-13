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
        super().__init__(*args, **kwargs)

        # Todos los vuelos y pasajeros
        self.fields['flight_id'].queryset = Flight.objects.all()
        self.fields['passenger_id'].queryset = Passenger.objects.all()

        # Filtrar asientos disponibles según el vuelo elegido
        flight_id = None
        if 'flight_id' in self.data:
            try:
                flight_id = int(self.data.get('flight_id'))
            except (ValueError, TypeError):
                pass

        if flight_id:
            flight = Flight.objects.get(id=flight_id)
            self.fields['seating_id'].queryset = Seating.objects.filter(
                airplane_id=flight.airplane_id,
                state=False
            )
        else:
            # Mostrar todos los asientos libres si no se seleccionó vuelo
            self.fields['seating_id'].queryset = Seating.objects.filter(state=False)

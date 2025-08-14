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

        # Aplicar clases Bootstrap
        self.fields['flight_id'].widget.attrs.update({'class': 'form-select'})
        self.fields['passenger_id'].widget.attrs.update({'class': 'form-select'})
        self.fields['seating_id'].widget.attrs.update({'class': 'form-select'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

        # Cargar vuelos y pasajeros
        self.fields['flight_id'].queryset = Flight.objects.all()
        self.fields['passenger_id'].queryset = Passenger.objects.all()

        # Filtrar asientos disponibles según vuelo
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
            self.fields['seating_id'].queryset = Seating.objects.filter(state=False)

    def clean(self):
        cleaned_data = super().clean()
        flight = cleaned_data.get('flight_id')
        price = cleaned_data.get('price')
        if flight and price is not None:
            base_price = flight.base_price
            if price < base_price:
                self.add_error('price', f'El precio debe ser igual o mayor al precio base del vuelo (${base_price}).')
        return cleaned_data

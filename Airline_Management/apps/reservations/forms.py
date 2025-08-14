from django import forms
from apps.flights.models import Flight
from apps.passengers.models import Passenger
from apps.airplanes.models import Seating
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['flight_id', 'passenger_id', 'seating_id', 'price']
        widgets = {
            'flight_id': forms.Select(attrs={'class': 'form-select'}),
            'passenger_id': forms.Select(attrs={'class': 'form-select'}),
            'seating_id': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        flight_instance = kwargs.pop('flight_instance', None)
        super().__init__(*args, **kwargs)
        self.fields['flight_id'].queryset = Flight.objects.all()
        self.fields['passenger_id'].queryset = Passenger.objects.all()

        # Filtrar asientos según el avión del vuelo seleccionado
        if flight_instance:
            self.fields['seating_id'].queryset = Seating.objects.filter(
                airplane_id=flight_instance.airplane_id,
                state=False
            )
        elif 'flight_id' in self.data:
            try:
                flight_id = int(self.data.get('flight_id'))
                flight = Flight.objects.get(pk=flight_id)
                self.fields['seating_id'].queryset = Seating.objects.filter(
                    airplane_id=flight.airplane_id,
                    state=False
                )
            except (ValueError, TypeError, Flight.DoesNotExist):
                self.fields['seating_id'].queryset = Seating.objects.none()
        elif self.instance.pk and self.instance.flight_id:
            flight = self.instance.flight_id
            self.fields['seating_id'].queryset = Seating.objects.filter(
                airplane_id=flight.airplane_id,
                state=False
            )
        else:
            self.fields['seating_id'].queryset = Seating.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        flight = cleaned_data.get('flight_id')
        price = cleaned_data.get('price')
        if flight and price is not None:
            base_price = flight.base_price
            if price < base_price:
                self.add_error('price', f'El precio debe ser igual o mayor al precio base del vuelo (${base_price}).')
        return cleaned_data
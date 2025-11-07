from django_filters import rest_framework as filters
from apps.flights.models import Flight

class FlightFilter(filters.FilterSet):
    # Ajusta field_name si tus campos se llaman distinto en el modelo Flight
    date = filters.DateFilter(field_name='departure_date', lookup_expr='date', label='Fecha')
    origin = filters.CharFilter(field_name='origin', lookup_expr='icontains', label='Origen')
    destination = filters.CharFilter(field_name='destination', lookup_expr='icontains', label='Destino')

    class Meta:
        model = Flight
        fields = ['date', 'origin', 'destination']
from django_filters import rest_framework as filters
from apps.reservations.models import Reservation

class ReservationFilter(filters.FilterSet):
    passenger = filters.NumberFilter(field_name='passenger__id', lookup_expr='exact', label='ID del Pasajero')
    flight = filters.NumberFilter(field_name='flight__id', lookup_expr='exact', label='ID del Vuelo')
    seat = filters.CharFilter(field_name='seat', lookup_expr='exact', label='Asiento')
    status = filters.ChoiceFilter(field_name='status', label='Estado')

    class Meta:
        model = Reservation
        fields = ['passenger', 'flight', 'seat', 'status']
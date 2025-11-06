from rest_framework import serializers
from apps.passengers.models import Passenger
from apps.reservations.models import Reservation
from apps.api.serializers.serializers_reservations import ReservationSerializer

class PassengerSerializer(serializers.ModelSerializer):
    # devuelve las reservas asociadas al passenger (intenta related_name 'reservations' y fallback a reservation_set)
    reservations = serializers.SerializerMethodField()

    class Meta:
        model = Passenger
        fields = '__all__'  # el campo 'reservations' declarado arriba se incluirá automáticamente

    def get_reservations(self, obj):
        # intenta obtener queryset por related_name 'reservations', si no existe usa reservation_set
        related_qs = getattr(obj, 'reservations', None)
        if related_qs is None:
            related_qs = getattr(obj, 'reservation_set', Reservation.objects.none())
        qs = related_qs.all() if hasattr(related_qs, 'all') else related_qs
        return ReservationSerializer(qs, many=True).data
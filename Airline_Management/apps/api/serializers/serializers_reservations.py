from rest_framework import serializers
from apps.reservations.models import Reservation, Ticket
from apps.passengers.models import Passenger
from apps.flights.models import Flight

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, attrs):
        flight = attrs.get('flight') or getattr(self.instance, 'flight', None)
        seat = attrs.get('seat') or getattr(self.instance, 'seat', None)
        # validar asiento ocupado en el mismo vuelo
        if flight and seat:
            qs = Reservation.objects.filter(flight=flight, seat=seat)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError({'seat': 'Asiento ya reservado para ese vuelo.'})
        return attrs

class TicketSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ['code', 'reservation', 'issued_at']
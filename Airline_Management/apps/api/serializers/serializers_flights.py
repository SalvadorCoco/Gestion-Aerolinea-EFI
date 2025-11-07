from rest_framework import serializers
from rest_framework import serializers
from apps.flights.models import Flight
from apps.airplanes.models import Seating
from apps.reservations.models import Reservation

class SeatInfoSerializer(serializers.ModelSerializer):
    is_reserved = serializers.SerializerMethodField()

    class Meta:
        model = Seating
        fields = ['number', 'row', 'column', 'type', 'state', 'is_reserved']

    def get_is_reserved(self, obj):
        flight_id = self.context.get('flight_id')
        if flight_id:
            return Reservation.objects.filter(
                flight_id=flight_id,
                seat=str(obj.number)
            ).exists()
        return False

class FlightSerializer(serializers.ModelSerializer):
    seats = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = '__all__'

    def get_seats(self, obj):
        seats = obj.airplane_id.seatings.all()
        return SeatInfoSerializer(seats, many=True, context={'flight_id': obj.id}).data
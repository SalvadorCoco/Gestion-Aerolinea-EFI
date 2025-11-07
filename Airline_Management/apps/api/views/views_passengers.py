from rest_framework import generics
from apps.passengers.models import Passenger
from apps.reservations.models import Reservation
from apps.api.serializers.serializers_passengers import PassengerSerializer
from apps.api.serializers.serializers_reservations import ReservationSerializer

class PassengerListCreateView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerActiveReservationsView(generics.ListAPIView):
    """
    GET /api/passengers/<pk>/reservations/?status=confirmed
    """
    serializer_class = ReservationSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        status_q = self.request.query_params.get('status')  # opcional, por defecto sólo activas/confirmed
        qs = Reservation.objects.filter(passenger_id=pk)
        if status_q:
            qs = qs.filter(status=status_q)
        else:
            qs = qs.filter(status__in=['confirmed', 'active', 'paid'])
        return qs
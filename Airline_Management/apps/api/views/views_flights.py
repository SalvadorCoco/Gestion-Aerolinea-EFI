from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from apps.flights.models import Flight
from apps.passengers.models import Passenger
from apps.reservations.models import Reservation
from apps.api.serializers.serializers_flights import FlightSerializer
from apps.api.serializers.serializers_flights import SeatInfoSerializer
from apps.api.serializers.serializers_passengers import PassengerSerializer
from apps.api.serializers.serializers_reservations import ReservationSerializer
from apps.api.filters.filters_flights import FlightFilter

@extend_schema(tags=['Flights'])
class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filterset_class = FlightFilter

    @extend_schema(
        parameters=[
            OpenApiParameter(name='date', description='Filter by departure date (YYYY-MM-DD)'),
            OpenApiParameter(name='origin', description='Filter by origin city'),
            OpenApiParameter(name='destination', description='Filter by destination city'),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

@extend_schema(tags=['Flights'])
class FlightRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # Flight detail uses the default GET/PUT/PATCH/DELETE handlers from RetrieveUpdateDestroyAPIView


@extend_schema(tags=['Flights'])
class FlightSeatsView(APIView):
    """GET /api/flights/<pk>/seats/ -> devuelve disposición de asientos y si están reservados"""
    @extend_schema(
        operation_id='get_flight_seats',
        description='Get seating layout for a specific flight',
        responses={200: SeatInfoSerializer(many=True)}
    )
    def get(self, request, pk):
        try:
            flight = Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            return Response({'detail': 'Flight not found.'}, status=status.HTTP_404_NOT_FOUND)
        seats = flight.airplane_id.seatings.all()
        serializer = SeatInfoSerializer(seats, many=True, context={'flight_id': pk})
        return Response(serializer.data)


@extend_schema(tags=['Flights'])
class FlightSeatDetailView(APIView):
    """GET /api/flights/<pk>/seats/<seat_number>/ -> estado de un asiento específico"""

    @extend_schema(
        operation_id='get_flight_seat_detail',
        description='Get status of a specific seat in a flight',
        responses={200: SeatInfoSerializer}
    )
    def get(self, request, pk, seat_number):
        try:
            flight = Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            return Response({'detail': 'Flight not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            seat = flight.airplane_id.seatings.get(number=seat_number)
        except Exception:
            return Response({'detail': 'Seat not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SeatInfoSerializer(seat, context={'flight_id': pk})
        return Response(serializer.data)

class FlightPassengersListView(generics.ListAPIView):
    """
    GET /api/flights/<pk>/passengers/  -> lista de passengers asociados por reservas (opcional filter status)
    """
    serializer_class = PassengerSerializer

    def get_queryset(self):
        flight_pk = self.kwargs.get('pk')
        status_q = self.request.query_params.get('status')  # opcional
        qs = Passenger.objects.filter(reservation__flight_id=flight_pk)
        if status_q:
            qs = qs.filter(reservation__status=status_q)
        return qs.distinct()

class FlightReserveView(APIView):
    """
    POST /api/flights/<pk>/reserve/
    Body: { "passenger": <id>, "seat": "12A", "status": "pending" }
    Crea una reservation vinculada al flight.
    """
    def post(self, request, pk):
        try:
            flight = Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            return Response({'detail': 'Flight not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['flight'] = pk
        serializer = ReservationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)
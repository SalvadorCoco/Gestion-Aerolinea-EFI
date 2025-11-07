from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter

from apps.reservations.models import Reservation, Ticket
from apps.api.serializers.serializers_reservations import ReservationSerializer, TicketSerializer
from apps.api.filters.filters_reservations import ReservationFilter


@extend_schema(tags=['Reservations'])
class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filterset_class = ReservationFilter

    @extend_schema(
        parameters=[
            OpenApiParameter(name='passenger', description='Filter by passenger ID'),
            OpenApiParameter(name='flight', description='Filter by flight ID'),
            OpenApiParameter(name='seat', description='Filter by seat number'),
            OpenApiParameter(name='status', description='Filter by reservation status'),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@extend_schema(tags=['Reservations'])
class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationStatusUpdateView(APIView):
    """
    PATCH /api/reservations/<pk>/status/  -> { "status": "confirmed" }
    """
    def patch(self, request, pk):
        try:
            res = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response({'detail': 'Reservation not found.'}, status=status.HTTP_404_NOT_FOUND)
        status_value = request.data.get('status')
        if not status_value:
            return Response({'status': 'required'}, status=status.HTTP_400_BAD_REQUEST)
        setattr(res, 'status', status_value)
        res.save()
        return Response(ReservationSerializer(res).data)

class TicketGenerateView(APIView):
    """
    POST /api/reservations/<pk>/ticket/  -> genera y guarda un Ticket si la reserva está confirmada
    """
    def post(self, request, pk):
        try:
            res = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response({'detail': 'Reservation not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Ajustá el valor aceptado para "confirmada"
        current_status = getattr(res, 'status', '').lower() if getattr(res, 'status', None) else ''
        if current_status not in ('confirmed', 'active', 'paid'):
            return Response({'detail': 'Reservation not confirmed. Cannot issue ticket.'}, status=status.HTTP_400_BAD_REQUEST)

        # Si ya existe un ticket, devolverlo
        if hasattr(res, 'ticket'):
            return Response(TicketSerializer(res.ticket).data)

        ticket = Ticket.objects.create(reservation=res)
        return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)

class TicketRetrieveView(generics.RetrieveAPIView):
    """
    GET /api/tickets/<code>/
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'code'
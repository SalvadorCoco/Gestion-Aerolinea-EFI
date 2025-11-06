from rest_framework import generics
from rest_framework.response import Response
import string

from apps.airplanes.models import Airplane
from apps.api.serializers.serializers_airplanes import AirplaneSerializer
from apps.reservations.models import Reservation  # usado para verificar reservas (ajustar si campos difieren)

class AirplaneListCreateView(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class AirplaneRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class AirplaneLayoutView(generics.RetrieveAPIView):
    """
    Devuelve el layout de asientos del avión y su disponibilidad.
    Opcional: ?flight=<id> para marcar asientos reservados en ese vuelo.
    Resultado ejemplo:
    {
      "airplane_id": 1,
      "layout": [
        {"row": 1, "seats": [{"label": "1A", "available": true}, {"label": "1B", "available": false}]},
        ...
      ]
    }
    NOTA: El código asume que:
      - el modelo Airplane puede tener `seat_map` (JSON/list) o `rows` y `seats_per_row`.
      - las reservas están en apps.reservations.models.Reservation con campo `seat` y `flight` (ajustar si difiere).
    """
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def retrieve(self, request, *args, **kwargs):
        airplane = self.get_object()
        flight_id = request.query_params.get('flight')

        # obtener asientos reservados para el vuelo (si se pasó flight)
        reserved = set()
        if flight_id:
            # Ajustar nombres de campo de Reservation si son distintos
            reserved_qs = Reservation.objects.filter(flight_id=flight_id)
            reserved = set(getattr(r, 'seat', None) for r in reserved_qs if getattr(r, 'seat', None))

        layout = []

        # Opción 1: seat_map en el modelo (espera lista/dict con filas)
        seat_map = getattr(airplane, 'seat_map', None)
        if seat_map:
            # seat_map esperado: [{"row": 1, "seats": ["1A","1B",...]}, ...]
            for row in seat_map:
                seats = []
                for label in row.get('seats', []):
                    seats.append({'label': label, 'available': label not in reserved})
                layout.append({'row': row.get('row'), 'seats': seats})
            return Response({'airplane_id': airplane.pk, 'layout': layout})

        # Opción 2: filas y asientos por fila (rows, seats_per_row)
        rows = getattr(airplane, 'rows', None)
        seats_per_row = getattr(airplane, 'seats_per_row', None)
        if rows and seats_per_row:
            letters = list(string.ascii_uppercase)
            for r in range(1, int(rows) + 1):
                seats = []
                for c in range(int(seats_per_row)):
                    label = f"{r}{letters[c]}"
                    seats.append({'label': label, 'available': label not in reserved})
                layout.append({'row': r, 'seats': seats})
            return Response({'airplane_id': airplane.pk, 'layout': layout})

        # Opción 3: fallback vacío (o implementar relación Seat)
        return Response({'airplane_id': airplane.pk, 'layout': layout})

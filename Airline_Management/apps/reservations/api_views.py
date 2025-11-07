from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# usa el serializer que ya está en apps/api/serializers
from apps.api.serializers.serializers_reservations import ReservationSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_reservation_api(request):
    """
    Endpoint protegido por JWT. Enviar JSON con los campos que espera ReservationSerializer.
    Ajusta serializer.save(...) si tu modelo necesita user=request.user u otros campos.
    """
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        # si la reserva tiene campo user/owner comenta/ajusta la siguiente línea:
        try:
            serializer.save(user=request.user)
        except TypeError:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
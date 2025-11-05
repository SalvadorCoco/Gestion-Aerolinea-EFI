from apps.airplanes.models import (Airplane, Seating)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.response import Response
from rest_framework import status
from ..serializers.serializers_airplanes import AirplaneSerializer

class AirplaneListCreateView(ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class AirplaneRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    
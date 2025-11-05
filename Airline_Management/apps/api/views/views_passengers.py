from rest_framework import generics
from apps.passengers.models import Passenger
from apps.api.serializers.serializers_passengers import PassengerSerializer

class PassengerListCreateView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
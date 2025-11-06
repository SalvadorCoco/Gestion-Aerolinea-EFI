from rest_framework import serializers
from apps.airplanes.models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'

# Filter serializer para validar query params
class AirplaneFilterSerializer(serializers.Serializer):
    date = serializers.DateField(required=False)           # ?date=2025-11-05
    origin = serializers.CharField(required=False)         # ?origin=EZE
    destination = serializers.CharField(required=False)    # ?destination=JFK
from apps.airplanes.models import (Airplane, Seating)
from rest_framework import serializers

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['pk', 'model', 'image', 'capacity', 'rows', 'columns']
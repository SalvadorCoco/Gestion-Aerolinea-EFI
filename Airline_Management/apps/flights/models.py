from django.db import models
from apps.airplanes.models import Airplane
from apps.accounts.models import Account
from apps.passengers.models import Passenger

# Create your models here.


FLIGHT_STATUS_CHOICES = [
    ('Programado', 'Programado'),
    ('En vuelo', 'En vuelo'),
    ('Aterrizado', 'Aterrizado'),
    ('Cancelado', 'Cancelado'),
]

class Flight(models.Model):
    airplane_id = models.ForeignKey(
        Airplane,
        on_delete=models.CASCADE,
        related_name='flights'
    )
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flights/', blank=True, null=True)
    departure_date = models.DateTimeField(auto_now_add=True)
    arrival_date = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=20, choices=FLIGHT_STATUS_CHOICES, default='Programado')
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.origin} → {self.destination} ({self.arrival_date.date()})'
    



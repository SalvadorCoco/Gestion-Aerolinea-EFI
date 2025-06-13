from django.db import models

from apps.airplanes.models import Seating
from apps.flights.models import Flight
from apps.passengers.models import Passenger

# Create your models here.
class Reservation(models.Model):
    flight_id = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE
    )
    passenger_id = models.ForeignKey(
        Passenger,
        on_delete=models.CASCADE
    )
    seating_id = models.OneToOneField(
        Seating,
        on_delete=models.CASCADE
    )
    state = models.CharField(max_length=20, default='Reserved')
    reservation_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    reservation_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.reservation_code} - {self.passenger_id.name}'
    
class Ticket(models.Model):
    reservation_id = models.OneToOneField(
        Reservation,
        on_delete=models.CASCADE
    )
    barcode = models.CharField(max_length=50)
    issue_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=20, default='Emitido')

    def __str__(self):
        return f'Ticket - {self.reservation_id.reservation_code}'
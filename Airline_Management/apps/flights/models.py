from django.db import models
from apps.airplanes.models import Airplane
from apps.accounts.models import Account

# Create your models here.

class Flight(models.Model):
    airplane_id = models.ForeignKey(
        Airplane,
        on_delete=models.CASCADE,
        related_name='flights'
    )
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateTimeField(auto_now_add=True)
    arrival_date = models.DateTimeField()
    duration = models.DurationField()
    state = models.BooleanField(default=False)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    account_flight = models.ManyToManyField(Account, blank=True)

    def __str__(self):
        return f'Flight: {self.origin} - {self.destination} - {self.departure_date}'
    



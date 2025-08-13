from django.db import models
import random
import string

from apps.airplanes.models import Seating
from apps.flights.models import Flight
from apps.passengers.models import Passenger

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

    def save(self, *args, **kwargs):
        # Generar código de reserva si no existe
        if not self.reservation_code:
            self.reservation_code = self._generate_unique_code()

        super().save(*args, **kwargs)

        # Marcar asiento como ocupado
        if self.seating_id and self.seating_id.state is False:
            self.seating_id.state = True
            self.seating_id.save()

    def delete(self, *args, **kwargs):
        # Liberar asiento
        if self.seating_id and self.seating_id.state is True:
            self.seating_id.state = False
            self.seating_id.save()
        super().delete(*args, **kwargs)

    def _generate_unique_code(self):
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not Reservation.objects.filter(reservation_code=code).exists():
                return code

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

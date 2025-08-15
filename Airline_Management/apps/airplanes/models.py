from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

SEATING_TYPE_CHOICES = [
    ('Normal', 'Normal'),
    ('Window', 'Ventana'),
    ('Aisle', 'Pasillo'),
    ('Exit', 'Salida de Emergencia'),
]

class Airplane(models.Model):
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='airplanes/', blank=True, null=True)
    capacity = models.IntegerField()
    rows = models.IntegerField()
    columns = models.IntegerField()

    def save(self, *args, **kwargs):
        max_columns = 8
        if self.capacity:
            self.columns = min(self.capacity, max_columns)
            self.rows = (self.capacity // self.columns) + (1 if self.capacity % self.columns else 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model


class Seating(models.Model):
    airplane_id = models.ForeignKey(
        Airplane,
        on_delete=models.CASCADE,
        related_name='seatings',
    )
    number = models.IntegerField()
    row = models.IntegerField()
    column = models.IntegerField()
    type = models.CharField(max_length=100, choices=SEATING_TYPE_CHOICES, default='Normal')
    state = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.number} ({self.type})"


@receiver(post_save, sender=Airplane)
def create_seatings(sender, instance, created, **kwargs):
    if created:  
        seat_number = 1
        for row in range(1, instance.rows + 1):
            for col in range(1, instance.columns + 1):
                if seat_number > instance.capacity:
                    break
                Seating.objects.create(
                    airplane_id=instance,
                    number=seat_number,
                    row=row,
                    column=col
                )
                seat_number += 1
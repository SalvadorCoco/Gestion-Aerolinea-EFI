from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

SEATING_TYPE_CHOICES = [
    ('Normal', 'Normal'),
    ('VIP', 'VIP'),
]

class Airplane(models.Model):
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='airplanes/', blank=True, null=True)
    capacity = models.IntegerField()
    rows = models.IntegerField(null=True)
    columns = models.IntegerField(null=True)

    def __str__(self):
        return self.model

    def save(self, *args, **kwargs):
        if self.capacity and (self.rows is None or self.columns is None):
            # Ejemplo: 6 columnas por fila
            self.columns = 6
            self.rows = (self.capacity // self.columns) + (1 if self.capacity % self.columns else 0)
        super().save(*args, **kwargs)

class Seating(models.Model):
    airplane_id = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    row = models.IntegerField()
    column = models.IntegerField()
    type = models.CharField(max_length=10, choices=SEATING_TYPE_CHOICES, default='Normal')
    state = models.BooleanField(default=False)  # False = disponible, True = ocupado

    def __str__(self):
        return f"Asiento {self.number} ({self.type})"

@receiver(post_save, sender=Airplane)
def create_seats_for_plane(sender, instance, created, **kwargs):
    if created:
        # Genera asientos automáticamente según filas y columnas
        for row in range(1, (instance.rows or 0) + 1):
            for col in range(1, (instance.columns or 0) + 1):
                number = f"{row}{chr(64 + col)}"  # Ejemplo: 1A, 1B, ...
                # Los primeros asientos de cada fila serán VIP 
                seat_type = 'VIP' if col == 1 else 'Normal'
                Seating.objects.create(
                    airplane_id=instance,
                    number=number,
                    row=row,
                    column=col,
                    type=seat_type
                )




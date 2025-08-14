from django.db import models
import math
from django.forms import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
import string

# Create your models here.

class Airplane(models.Model):
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='airplanes/', blank=True, null=True)
    capacity = models.IntegerField()
    rows = models.IntegerField(null=True)
    columns = models.IntegerField(null=True)

    def __str__(self):
        return self.model
    
    def clean(self):
        if self.capacity and self.capacity > 500:
            raise ValidationError({'capacity': 'La capacidad máxima permitida es 500 pasajeros.'})
        if self.columns is not None and self.columns > 9:
            raise ValidationError({'columns': 'El máximo de columnas permitido es 9.'})
        if self.rows and self.columns and self.capacity != self.rows * self.columns:
            raise ValidationError({
                'capacity': 'La capacidad debe ser igual a filas x columnas.'
            })
    
    def save(self, *args, **kwargs):
        if self.capacity > 500:
            self.capacity = 500
        if (not self.rows or not self.columns or self.columns > 9) and self.capacity:
            self.rows, self.columns = self._calculate_rows_columns(self.capacity)
        elif self.rows and self.columns:
            self.capacity = self.rows * self.columns
        super().save(*args, **kwargs)


    @staticmethod
    def _calculate_rows_columns(capacity):
        max_columns = 9
        for columns in range(max_columns, 0, -1):
            if capacity % columns == 0:
                rows = capacity // columns
                return rows, columns
        columns = max_columns
        rows = math.ceil(capacity / columns)
        return rows, columns
    
@receiver(post_save, sender=Airplane)
def create_seats_for_plane(sender, instance, created, **kwargs):
    if created:
        # Evitar duplicados
        if Seating.objects.filter(Airplane=instance).exists():
            return
        # Crear asientos según filas y columnas
        for row in range(1, instance.rows + 1):
            for col in range(1, instance.columns + 1):
                col_letter = string.ascii_uppercase[col - 1]
                Seating.objects.create(
                    Airplane=instance,
                    number=f"{row}{col_letter}",
                    row=row,
                    column=col_letter,
                    type='economy',
                    status='available'
                )



SEATING_TYPE_CHOICES = [
    ('Normal', 'Normal'),
    ('VIP', 'VIP'),
]

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
        return f"Seating: {self.number} ({self.type})"
    



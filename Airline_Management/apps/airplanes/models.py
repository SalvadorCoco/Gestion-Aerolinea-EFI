from django.db import models

# Create your models here.

class Airplane(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    rows = models.IntegerField()
    columns = models.IntegerField()

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
    type = models.CharField(max_length=100)
    state = models.BooleanField(default=False)

    def __str__(self):
        return f"Seating: {self.number} ({self.type})"
    



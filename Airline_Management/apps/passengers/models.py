from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_birth = models.DateField()
    document_type = models.CharField(max_length=50)

    def __str__(self):
        return f'Name: {self.name} - Document: {self.document}'

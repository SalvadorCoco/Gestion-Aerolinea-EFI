from django.db import models


DOCUMENT_TYPE_CHOICES = [
    ('DNI', 'DNI'),
    ('Pasaporte', 'Pasaporte'),
    ('Cedula', 'Cédula'),
]

class Passenger(models.Model): 
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_birth = models.DateField()
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES)

    def __str__(self):
        return self.name
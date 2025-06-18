from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

    
class Role(models.Model):
    description = models.CharField(max_length=100) 

    def __str__(self):
        return self.description
    
class Account(AbstractUser):
    role_id = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='role',
        null=True
    )
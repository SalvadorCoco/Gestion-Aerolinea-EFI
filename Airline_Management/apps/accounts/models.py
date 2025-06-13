from django.db import models

# Create your models here.

    
class Role(models.Model):
    description = models.CharField(max_length=100) 

    def __str__(self):
        return self.description
    
class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return self.username
# api/models.py
from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    messagetext = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    session_key = models.CharField(max_length=40)  # tie to session

    def __str__(self):
        return self.name

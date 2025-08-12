
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    amenities = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name}, {self.city}"

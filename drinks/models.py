from unicodedata import name
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # This will be rendered when we make a request and instead of instance will be returned the 
    # instance attribute will be displayed
    def __str__(self):
        return f"{self.name} {self.description}"
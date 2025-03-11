from django.db import models

# Create your models here.
class Menu(models.model):
    Name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
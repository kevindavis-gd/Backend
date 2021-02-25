from django.db import models

# Create your models here.
class CheckIn(models.Model):
    mustangsID = models.CharField(max_length=100)
    buildingID = models.CharField(max_length=100)
    checkIn = models.CharField(max_length=100)
    scanTime = models.CharField(max_length=100)


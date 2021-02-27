from django.db import models

# Test class to endure that the api works
# Inherits from the default model class and sets the requirements for the database columns
class CheckIn(models.Model):
    mustangsID = models.CharField(max_length=100)
    buildingID = models.CharField(max_length=100)
    checkIn = models.CharField(max_length=100)
    scanTime = models.CharField(max_length=100)


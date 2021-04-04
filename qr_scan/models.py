from django.db import models
from locations.models import Building

#//////////////////////////////////////////////////////////////////////////
#///////////////////this is the actual checkin class///////////////////////
#//////////////////////////////////////////////////////////////////////////
# Inherits from the default model class and sets the requirements for the database columns

class CheckIn(models.Model):
    mustangsID = models.CharField(max_length=100)
    checkInTime = models.CharField(max_length=100)
    checkOutTime = models.CharField(max_length=100)
    scanDate = models.CharField(max_length=100)
    room = models.ForeignKey('locations.Room', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return (self.mustangsID + " | " + self.scanDate + " | " + self.checkInTime)

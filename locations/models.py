from django.db import models

# Inherits from the default model class and sets the requirements for the database columns
class Campus(models.Model):
    campusID = models.CharField(max_length=100, unique= True)
    campusName = models.CharField(max_length=100, unique= True)
    #campusLocation = models.Location

    class Meta:
        verbose_name_plural = 'Campuses'
    
    def __str__(self):
        return self.campusName


class Building(models.Model):
    buildingID  = models.CharField(max_length=100, unique= True)
    buildingName = models.CharField(max_length=100, unique= True)
    #buildingLocation = models.CharField(max_length=100)
    buildingCapacity = models.IntegerField()
    numberOfRooms = models.IntegerField()
    campus = models.ForeignKey('Campus', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.buildingName


class Room(models.Model):
    roomID = models.CharField(max_length=100, unique= True)
    roomName = models.CharField(max_length=100, unique= True)
    roomCapacity = models.IntegerField()
    building = models.ForeignKey('Building', default=None, on_delete=models.CASCADE)
    #def __str__(self):
        #return self.roomName


class Equipment(models.Model):
    equipmentID = models.CharField(max_length=100)
    equipmentName = models.CharField(max_length=100)
    room = models.ForeignKey('Room', default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Equipment'
    
    def __str__(self):
        return self.equipmentName
from django.db import models

# Inherits from the default model class and sets the requirements for the database columns
class Campus(models.Model):
    campusID = models.CharField(max_length=100)
    campusName = models.CharField(max_length=100)
    campusLocation = models.CharField(max_length=100)


class Building(models.Model):
    buildingID = models.CharField(max_length=100)
    buildingName = models.CharField(max_length=100)
    buildingLocation = models.CharField(max_length=100)
    buildingCapacity = models.CharField(max_length=100)
    numberOfRooms = models.CharField(max_length=100)


class Room(models.Model):
    roomID = models.CharField(max_length=100)
    roomName = models.CharField(max_length=100)
    roomCapacity = models.CharField(max_length=100)


class Equipment(models.Model):
    equipmentID = models.CharField(max_length=100)
    equipmentName = models.CharField(max_length=100)
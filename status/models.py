from django.db import models

# Inherits from the default model class and sets the requirements for the database columns
class Date(models.Model):
    date = models.CharField(max_length=100)
    numberOfPeople = models.IntegerField
    

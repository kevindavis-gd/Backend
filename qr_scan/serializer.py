#convert python to json and vice versa

from rest_framework import serializers
from .models import CheckIn

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('mustangsID','buildingID','scanTime','scanDate')
        #permission_classes = [IsAuthenticated,]

class getCheckinsFor(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('mustangsID','buildingID','scanTime','scanDate')
        #permission_classes = [IsAuthenticated,]
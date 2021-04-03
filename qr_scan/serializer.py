#convert python to json and vice versa

from rest_framework import serializers
from .models import CheckIn

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('mustangsID','room')
        #permission_classes = [IsAuthenticated,]


class getCheckinsForSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('mustangsID','room','checkInTime','scanDate')
        #permission_classes = [IsAuthenticated,]
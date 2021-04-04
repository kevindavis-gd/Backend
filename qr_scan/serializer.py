#convert python to json and vice versa

from rest_framework import serializers
from .models import CheckIn

#//////////////////////////////////////////////////////////////////////////
#serialize the Checkin data into the listed fields to store into the database
#//////////////////////////////////////////////////////////////////////////
class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('mustangsID','room')
        #permission_classes = [IsAuthenticated,]

#//////////////////////////////////////////////////////////////////////////
#serialize the Checkin data into the listed fields to send to the frontend
#//////////////////////////////////////////////////////////////////////////
class getCheckinsForSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('mustangsID','room','checkInTime','scanDate')
        #permission_classes = [IsAuthenticated,]
#convert python to json and vice versa

from rest_framework import serializers
from .models import CheckIn
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from datetime import datetime


class CheckInSerializer(serializers.ModelSerializer):


    class Meta:
        model = CheckIn
        fields = ('mustangsID','buildingID','scanTime','scanDate')
        permission_classes = [IsAuthenticated,]
#convert python to json and vice versa

from rest_framework import serializers
from .models import Date


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('date')
        #permission_classes = [IsAuthenticated,]date
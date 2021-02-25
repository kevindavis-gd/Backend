from rest_framework import viewsets
from . import models
from . import serializer

class CheckInViewset(viewsets.ModelViewSet):
    queryset = models.CheckIn.objects.all()
    serializer_class = serializer.CheckInSerializer

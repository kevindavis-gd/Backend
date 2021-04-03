from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User
from qr_scan.models import CheckIn
from qr_scan.serializer import CheckInSerializer



class DateViewset(viewsets.ModelViewSet):
    queryset = models.Date.objects.all()
    serializer_class = serializer.DateSerializer

    @action(methods=['get'], detail=False)
    def getDateStatus(self, request):
        date = request.data['date']
        queryset = CheckIn.objects.filter(scanDate__exact = date)
        serializer_class = CheckInSerializer(queryset, many = True)
        return Response(serializer_class.data)

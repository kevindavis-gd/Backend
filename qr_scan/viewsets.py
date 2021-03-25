from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class CheckInViewset(viewsets.ModelViewSet):
    user = User.objects.get(username= "root")
    print(user.first_name)
    queryset = models.CheckIn.objects.all()
    serializer_class = serializer.CheckInSerializer



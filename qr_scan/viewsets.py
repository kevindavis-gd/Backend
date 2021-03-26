from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics


class CheckInViewset(viewsets.ModelViewSet):
    queryset = models.CheckIn.objects.all()
    serializer_class = serializer.CheckInSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('scanDate').last()
        serializer =self.get_serializer_class()(newest)
        print(request.user)
        return Response(serializer.data)


    @action(methods=['get'], detail=False)
    def getcheckins(self, request):
        #get the username by looking at the token sent from the front end
        username = request.user.get_username()
        #filter out the data by the username/mustangsID
        queryset = models.CheckIn.objects.filter(mustangsID__exact=username)
        serializer_class = serializer.CheckInSerializer(queryset, many = True)
        return Response(serializer_class.data)

   
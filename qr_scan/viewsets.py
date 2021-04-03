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

from datetime import datetime
from datetime import date
from datetime import datetime, timedelta
import re


class CheckInViewset(viewsets.ModelViewSet):
    queryset = models.CheckIn.objects.all()
    serializer_class = serializer.CheckInSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('scanDate').last()
        serializer =self.get_serializer_class()(newest)
        print(request.user)
        return Response(serializer.data)


    @action(methods=['post'], detail=False)
    def scan(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        username = request.user.get_username()
        
        inner_serializer = serializer.CheckInSerializer(data=request.data)
        previous_queryset = models.CheckIn.objects.filter(mustangsID__exact=username).last()

        current_Equipment_ID = request.data['room']
        previous_Equipment_ID = previous_queryset.room.roomID
        previous_checkout_time = previous_queryset.checkOutTime
        previous_checkin_date = previous_queryset.scanDate
        
        if previous_checkout_time  == "NONE" and previous_Equipment_ID == current_Equipment_ID and previous_checkin_date == current_date  :
            print('Checkout')
            inner_serializer = serializer.CheckInSerializer(instance = previous_queryset, data=request.data)
            inner_serializer.is_valid(self)
            inner_serializer.save(checkOutTime = current_time)
            return Response(inner_serializer.data)

        elif (previous_checkout_time  == "NONE" and previous_Equipment_ID != current_Equipment_ID) or (previous_checkout_time  == "NONE" and previous_checkin_date != current_date):
            print('differentID or different date')
            inner_serializer = serializer.CheckInSerializer(instance = previous_queryset, data=request.data)
            inner_serializer.is_valid(self)
            inner_serializer.save(checkOutTime = current_time)

            inner_serializer = serializer.CheckInSerializer(data=request.data)
            inner_serializer.is_valid(self)
            inner_serializer.save(checkInTime= current_time,scanDate = current_date, checkOutTime = "NONE")
            return Response(inner_serializer.data)

        else:
            print('new checkin')
            inner_serializer = serializer.CheckInSerializer(data=request.data)
            inner_serializer.is_valid(self)
            inner_serializer.save(checkInTime= current_time,scanDate = current_date, checkOutTime = "NONE")
            return Response(inner_serializer.data)



    @action(methods=['post'], detail=False)
    def create_checkin(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        inner_serializer = serializer.CheckInSerializer(data=request.data)
        inner_serializer.is_valid(self)
        inner_serializer.save(checkInTime= current_time, checkOutTime = "NO")
        return Response(inner_serializer.data)

    @action(methods=['post'], detail=False)
    def create_checkout(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        username = request.user.get_username()
        queryset = models.CheckIn.objects.filter(mustangsID__exact=username).last()
        serializer_class = serializer.CheckInSerializer(instance = queryset, data=request.data)
        serializer_class.is_valid(self)
        serializer_class.save(checkOutTime = current_time)
        return Response(serializer_class.data)
    
    @action(methods=['get'], detail=False)
    def getcheckins(self, request):
        #get the username by looking at the token sent from the front end
        username = request.user.get_username()
        staff = self.request.user.is_staff
        if staff:
            print("staff Access")
            queryset = models.CheckIn.objects.all()
        else:
            print("non-staff Access")
            #filter out the data by the username/mustangsID
            queryset = models.CheckIn.objects.filter(mustangsID__exact=username)
        serializer_class = serializer.getCheckinsForSerializer(queryset, many = True)
        return Response(serializer_class.data)


    @action(methods=['get'], detail=False)
    def getDateStatus(self, request):
        now = datetime.now() - timedelta(days = 1)
        listOfDays = []

        for x in range(0,14):
            now = datetime.now() - timedelta(days = x)
            current_date = now.strftime("%Y-%m-%d")
            queryset = models.CheckIn.objects.filter(scanDate__exact = current_date).count()
            listOfDays.append(queryset)
        return Response(listOfDays)


    @action(methods=['get'], detail=False)
    def getHourStatus(self, request):
        listOfHours = []

        for x in range(0,14):
            current_date = datetime.now() - timedelta(days = x)
            current_date_string = current_date.strftime("%Y-%m-%d")
            HourList = []
            for y in range(0,23):
                queryset = models.CheckIn.objects.filter(scanDate__exact = current_date_string).filter(checkInTime__regex =r'^' + str(y) + '.').count()
                print(queryset)
                HourList.append(queryset)
            listOfHours.append(HourList)
        return Response(listOfHours)





    @action(methods=['post'], detail=False)
    def getexposedpeople(self, request):
        import datetime
        #get the username by looking at the token sent from the front end
        username = request.data['username']
        finalQueryset = models.CheckIn.objects.none()
        print(username)
        staff = self.request.user.is_staff
        if staff:
            print("staff Access")
            queryset1 = models.CheckIn.objects.filter(mustangsID__exact=username)
            for x in queryset1:
                studentScanDate = x.scanDate
                if queryset1 != None:
                    queryset2 =  queryset1.filter(scanDate__exact = studentScanDate).filter(checkInTime__range=[x.checkInTime, x.checkOutTime])
                    if queryset2 != None:
                        queryset3 = queryset1.filter(scanDate__exact = studentScanDate).filter(checkOutTime__range=[x.checkInTime, x.checkOutTime])
                        
            print("non-staff Access")
            #filter out the data by the username/mustangsID
            serializer_class = serializer.getCheckinsForSerializer(queryset3, many = True)
            return Response(serializer_class.data)
        return Response("you are not staff")
        
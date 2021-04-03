from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta, date
import re


class CheckInViewset(viewsets.ModelViewSet):
    queryset = models.CheckIn.objects.all()
    serializer_class = serializer.CheckInSerializer

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////Get the last checkin//////////////////////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('scanDate').last()
        serializer =self.get_serializer_class()(newest)
        print(request.user)
        return Response(serializer.data)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #/////////////////////////////////////////////ScanQR//////////////////////////////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @action(methods=['post'], detail=False)
    def scan(self, request):
        #cet the date and time now
        now = datetime.now()
        #convert the time into a string
        current_time = now.strftime("%H:%M:%S")
        #cinvert the date into a string
        current_date = now.strftime("%Y-%m-%d")
        #get the username from the request sent
        username = request.user.get_username()

       
        #get the last checkin created by the user and store into a queryset
        previous_queryset = models.CheckIn.objects.filter(mustangsID__exact=username).last()

        #store the equipmentID/roomID of the current scan
        #####################################################
        #this needs to change from roomID to equipmentID
        #####################################################
        current_Equipment_ID = request.data['room'] ####################Change
        #store the equipmentID of the previous checkin
        previous_Equipment_ID = previous_queryset.room.roomID ####################Change
        #store the check out time of the previous checkin
        previous_checkout_time = previous_queryset.checkOutTime
        #store the scan date of the previous checkin
        previous_checkin_date = previous_queryset.scanDate
        
        #if the previous checkout time is "NONE" and the previous equipmentID is the same as the currentID
        #and the previous checkin date is the same as the current checkin date
        #that means this scan will be a checkout
        if previous_checkout_time  == "NONE" and previous_Equipment_ID == current_Equipment_ID and previous_checkin_date == current_date:
            print('Checkout')
            #store the same instance of the previous checkin into the queryset
            inner_serializer = serializer.CheckInSerializer(instance = previous_queryset, data=request.data)
            inner_serializer.is_valid(self)
            #save/update the instance of the previous checkin with a new checkout time
            inner_serializer.save(checkOutTime = current_time)
            return Response(inner_serializer.data)

        #if the previous checkout time is "NONE" and the previous equipmentID is not the ame as the current equipmentiD
        #or if the previou checkout time is "NONE" and the previous checkin date is not the same as the current checkin date
        #we need to checkout the previous checkin and create a new checkin

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
            #store the current data received into a queryset
            inner_serializer = serializer.CheckInSerializer(data=request.data)
            inner_serializer.is_valid(self)
            #save the new checkin with the current checkin time and current scanDate but set the CheckOutTime to NONE
            inner_serializer.save(checkInTime= current_time,scanDate = current_date, checkOutTime = "NONE")
            return Response(inner_serializer.data)

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #/////////////////////////////////////////////Get list of checkins////////////////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    @action(methods=['get'], detail=False)
    def getcheckins(self, request):
        #get the username by looking at the token sent from the front end
        username = request.user.get_username()
        #check if the user is a staff member
        staff = self.request.user.is_staff
        #if they are staff, give them access to all the checkin objects
        if staff:
            print("staff Access")
            queryset = models.CheckIn.objects.all().order_by('id').reverse()
        #if they are not staff only give acces to their checkins
        else:
            print("non-staff Access")
            #filter out the data by the username/mustangsID
            #orderby id in reverse, to show newest first
            queryset = models.CheckIn.objects.filter(mustangsID__exact=username).order_by('id').reverse()
        serializer_class = serializer.getCheckinsForSerializer(queryset, many = True)
        return Response(serializer_class.data)

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////Get number of chekins per day/////////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # the function below loops 14 times to get the current day minus 14 days.
    @action(methods=['get'], detail=False)
    def getDateStatus(self, request):

        listOfDays = []

        for x in range(0,14):
            #get the current date minus x number of days
            now = datetime.now() - timedelta(days = x)
            #converts the date into a string with a certain format
            current_date = now.strftime("%Y-%m-%d")
            # return the count of all the checkin objects that has the exact current_date
            queryset = models.CheckIn.objects.filter(scanDate__exact = current_date).count()
            listOfDays.append(queryset)
        print(listOfDays)
        return Response(listOfDays)

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////Get number of checkins per hour////////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # the function below loops 14 times to get the current day minus 14 days. 
    # and for each of the 14 loops, it loops 24 times for each hour.
    @action(methods=['get'], detail=False)
    def getHourStatus(self, request):
        listOfHours = []

        for x in range(0,14):
            #get the current date minus x number of days
            current_date = datetime.now() - timedelta(days = x)
            #converts the date into a string with a certain format
            current_date_string = current_date.strftime("%Y-%m-%d")
            # create a new list of hours every iteration
            HourList = []

            for y in range(0,23):
                # return the count of all the checkin objects that has the exact current_date and a checkin_time that starts with y (24 hour clock)
                queryset = models.CheckIn.objects.filter(scanDate__exact = current_date_string).filter(checkInTime__regex =r'^' + str(y) + '.').count()
                print(queryset)
                # add the information to the hour list
                HourList.append(queryset)

            # add the hour list to the listOfHours list creating a list of lists
            listOfHours.append(HourList)
        return Response(listOfHours)
        

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #the below function is not in use
'''
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
                        
            #filter out the data by the username/mustangsID
            serializer_class = serializer.getCheckinsForSerializer(queryset3, many = True)
            return Response(serializer_class.data)
        print("non-staff Access")
        return Response("you are not staff")
'''
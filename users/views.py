from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        #serialize the data sent from the front end
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #after the user is saved, create a token for the user
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
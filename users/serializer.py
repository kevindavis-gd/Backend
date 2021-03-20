from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

#User model already exists within Django, we just created the serializer
class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
            max_length=100
            )
    last_name = serializers.CharField(
            max_length=100
            )
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            required=True,
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password1 = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],email = validated_data['email'],password=validated_data['password1'],first_name = validated_data['first_name'],last_name = validated_data['last_name'])
        
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name','last_name','username', 'email', 'password1','password2')
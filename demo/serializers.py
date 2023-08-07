from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile_number', 'address', 'city', 'state',
                  'zip_code', 'date_of_birth', 'gender', 'profile_pic', 'hobbies']


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

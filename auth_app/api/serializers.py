from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    fullname = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    repeated_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError('Passwords do not match')
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['fullname']
        )

        return user
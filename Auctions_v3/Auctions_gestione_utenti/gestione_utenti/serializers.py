from rest_framework import serializers
from django.contrib.auth import get_user_model
from .forms import RegisterForm as forms

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'is_active', 'is_staff')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


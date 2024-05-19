# users/serializers.py

from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        """Hash the password before saving it."""
        return value  # Ensure password is hashed before saving

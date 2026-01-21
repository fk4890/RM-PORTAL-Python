from django.contrib.auth import authenticate
from rest_framework import serializers

from .messages import LoginMessages


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError(LoginMessages.TEMPLATES["INVALID_CREDENTIALS"])
        if not user.is_active:
            raise serializers.ValidationError(LoginMessages.TEMPLATES["INACTIVE_ACCOUNT"])
        attrs["user"] = user
        return attrs


class LoginResponseSerializer(serializers.Serializer):
    username = serializers.CharField()
    role = serializers.CharField()

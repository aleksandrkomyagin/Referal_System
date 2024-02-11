from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class Response200Serializer(serializers.Serializer):
    """200 response: create invite_code."""

    invite_code = serializers.CharField(default="string")

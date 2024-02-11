import re

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    code_by_inviter = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "code_by_inviter",
        )

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs


class UserSignupByInviteCodeSerializer(UserSignupSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inviter = None

    def validate(self, attrs):
        invite_code = attrs.pop("code_by_inviter")
        attrs = super().validate(attrs)

        try:
            self.inviter = User.objects.get(invite_code=invite_code)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "invite_code":
                    "Неверный инвайт-код или пользователь не существует."
                }
            )

        return attrs

    def validate_code_by_inviter(self, value):
        if not re.match(r"^[a-zA-Z0-9]{6}$", value):
            raise serializers.ValidationError("Некорректный инвайт-код")
        return value

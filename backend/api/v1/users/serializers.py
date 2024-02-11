from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.v1.users.utils import decrypt, encrypt

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class InviteCodeSerializer(serializers.Serializer):
    @staticmethod
    def get_referal_code(id: str, expiration_date: int) -> str:
        expiration_date = timezone.now() + timedelta(seconds=expiration_date)
        return f"referal-{encrypt(id, str(expiration_date))}"

    def create(self, validated_data):
        user = self.context["request"].user
        invite_code = self.get_referal_code(
            str(user.id), settings.ONE_WEEK_IN_SECONDS
        )
        user.invite_code = invite_code
        user.save()
        cache.set(
            user.id, (invite_code, user), timeout=settings.ONE_WEEK_IN_SECONDS
        )
        return user

    def to_representation(self, instance):
        return {"invite_code": instance.invite_code}


class GetInvitingsSerializer(serializers.ModelSerializer):
    invitings = UserSerializer(many=True)

    class Meta:
        model = User
        fields = ("invitings",)


class GetInviteCodeByEmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ("invite_code", "email")
        read_only_fields = ("email",)

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise ValidationError(
                {"email": "Неверный email или пользователь не существует."}
            )
        attrs["invite_code"] = user.invite_code
        return attrs


class InviteCodeActivateSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    invite_code = serializers.CharField(required=True)

    def validate(self, attrs):
        invite_code = attrs["invite_code"]
        id, expiration_date = decrypt(invite_code)
        data = cache.get(id)

        if data is None:
            raise ValidationError({"invite_code": "Неверный инвайт-код."})

        if timezone.now() > datetime.strptime(
            expiration_date, "%Y-%m-%d %H:%M:%S.%f%z"
        ):
            raise ValidationError({"invite_code": "Срок действия кода истек."})

        if self.instance.invite_code == invite_code:
            raise ValidationError(
                {
                    "invite_code":
                    "Недопустимо использовать собственный инвайт-код"
                }
            )

        if self.instance.inviter:
            raise ValidationError(
                {"invite_code": "Вы уже активировали один инвайт-код."}
            )

        attrs["inviter"] = data[1]

        return attrs

    def save(self, **kwargs):
        self.instance.inviter = kwargs["inviter"]
        self.instance.save()

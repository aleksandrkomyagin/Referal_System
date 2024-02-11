from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator)
from api.v1.users.serializers import (GetInviteCodeByEmailSerializer,
                                      GetInvitingsSerializer,
                                      InviteCodeActivateSerializer,
                                      InviteCodeSerializer)

User = get_user_model()


class InviteCodeBaseView(views.APIView):
    @staticmethod
    def get_user(pk=None):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise ValidationError(
                {"id": "Неверный id или пользователь не существует."}
            )


@get_drf_spectacular_view_decorator("users")
class InviteCodeView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = InviteCodeSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.invite_code = None
        user.save(update_fields=["invite_code"])
        return Response(
            {"invite_code": "Инвайт-код удален."}, status=status.HTTP_200_OK
        )


@get_drf_spectacular_view_decorator("users")
class GetInviteCodeByEmailView(views.APIView):
    def post(self, request):
        serializer = GetInviteCodeByEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invite_code = serializer.validated_data["invite_code"]
        return Response(
            {"invite_code": invite_code}, status=status.HTTP_200_OK
        )


@get_drf_spectacular_view_decorator("users")
class InviteCodeActivateView(views.APIView):
    def post(self, request):
        serializer = InviteCodeActivateSerializer(
            request.user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        inviter = serializer.validated_data["inviter"]
        serializer.save(**{"inviter": inviter})
        return Response(
            {"invite_code": "Инвайт-код активирован."},
            status=status.HTTP_200_OK,
        )


@get_drf_spectacular_view_decorator("users")
class GetUserByIDView(views.APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = GetInvitingsSerializer(user)
        return Response(serializer.data)

from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from api.v1.auth import serializers
from api.v1.drf_spectacular.custom_decorators import \
    get_drf_spectacular_view_decorator

User = get_user_model()


@get_drf_spectacular_view_decorator("auth")
class UserSignupView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        flag = False
        if "code_by_inviter" in request.data:
            serializer = serializers.UserSignupByInviteCodeSerializer(
                data=request.data
            )
            flag = True
        else:
            serializer = serializers.UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if flag:
            user.inviter = serializer.inviter
            user.save(update_fields=["inviter"])
        token = RefreshToken.for_user(user)
        return Response(
            {"access": str(token.access_token), "refresh": str(token)},
            status=status.HTTP_200_OK,
        )


@get_drf_spectacular_view_decorator("auth")
class RefreshTokenView(TokenRefreshView):
    pass

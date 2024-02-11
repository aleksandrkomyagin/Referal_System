from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer,
                                                  TokenRefreshSerializer)

from api.v1.auth.serializers import UserSignupByInviteCodeSerializer
from api.v1.drf_spectacular.serializers import (Response400Serializer,
                                                Response401Serializer)

AUTH_VIEW_DECORATORS = {
    "UserSignupView": extend_schema_view(
        post=extend_schema(
            tags=("auth",),
            request=UserSignupByInviteCodeSerializer,
            responses={
                status.HTTP_200_OK: TokenObtainPairSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "RefreshTokenView": extend_schema_view(
        post=extend_schema(
            tags=("auth",),
            request=TokenRefreshSerializer,
            responses={
                status.HTTP_200_OK: TokenRefreshSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
}

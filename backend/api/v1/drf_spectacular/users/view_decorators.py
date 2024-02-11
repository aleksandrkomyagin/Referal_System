from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from api.v1.drf_spectacular.serializers import (Response400Serializer,
                                                Response401Serializer)
from api.v1.drf_spectacular.users.serializers import Response200Serializer
from api.v1.users.serializers import (GetInviteCodeByEmailSerializer,
                                      GetInvitingsSerializer,
                                      InviteCodeActivateSerializer)

USERS_VIEW_DECORATORS = {
    "InviteCodeView": extend_schema_view(
        post=extend_schema(
            tags=("users",),
            responses={
                status.HTTP_201_CREATED: Response200Serializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        delete=extend_schema(
            tags=("users",),
        ),
    ),
    "GetInviteCodeByEmailView": extend_schema_view(
        post=extend_schema(
            tags=("users",),
            request=GetInviteCodeByEmailSerializer,
            responses={
                status.HTTP_200_OK: Response200Serializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "InviteCodeActivateView": extend_schema_view(
        post=extend_schema(
            tags=("users",),
            request=InviteCodeActivateSerializer,
            responses={
                status.HTTP_200_OK: InviteCodeActivateSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "GetUserByIDView": extend_schema_view(
        get=extend_schema(
            tags=("users",),
            request=GetInvitingsSerializer,
            responses={
                status.HTTP_200_OK: GetInvitingsSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
}

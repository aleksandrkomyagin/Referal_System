from django.urls import path

from api.v1.users.views import (GetInviteCodeByEmailView, GetUserByIDView,
                                InviteCodeActivateView, InviteCodeView)

urlpatterns = [
    path(
        "<int:user_id>/",
        GetUserByIDView.as_view(),
        name="invitings",
    ),
    path("invite_code/", InviteCodeView.as_view(), name="invite_code"),
    path(
        "get_invite_code_by_email/",
        GetInviteCodeByEmailView.as_view(),
        name="get_invite_code_by_email",
    ),
    path(
        "activate_invite_code/",
        InviteCodeActivateView.as_view(),
        name="activate_invite_code",
    ),
]

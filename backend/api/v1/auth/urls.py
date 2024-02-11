from django.urls import path

from api.v1.auth.views import RefreshTokenView, UserSignupView

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="signup"),
    path("refresh_token/", RefreshTokenView.as_view(), name="refresh_token"),
]

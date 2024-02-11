from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("auth/", include("api.v1.auth.urls")),
    path("users/", include("api.v1.users.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        "schema/docs/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="docs",
    ),
]

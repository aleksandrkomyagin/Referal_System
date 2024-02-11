from api.v1.drf_spectacular.auth.view_decorators import AUTH_VIEW_DECORATORS
from api.v1.drf_spectacular.users.view_decorators import USERS_VIEW_DECORATORS

VIEW_DECORATORS = {
    "auth": AUTH_VIEW_DECORATORS,
    "users": USERS_VIEW_DECORATORS,
}

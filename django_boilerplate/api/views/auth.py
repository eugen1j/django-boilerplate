from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenViewBase,
)

from django_boilerplate.api.serializers.auth import LogoutSerializer


class LoginView(TokenObtainPairView):
    pass


class RefreshView(TokenRefreshView):
    pass


class LogoutView(TokenViewBase):
    """
    Takes a refresh type JSON web token and invalidates it.
    """
    serializer_class = LogoutSerializer

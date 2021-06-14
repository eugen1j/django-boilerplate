from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenViewBase,
)

from django_boilerplate.api.serializers.auth import LogoutSerializer, UserSerializer


class LoginView(TokenObtainPairView):
    pass


class RefreshView(TokenRefreshView):
    pass


class LogoutView(TokenViewBase):
    """
    Takes a refresh type JSON web token and invalidates it.
    """

    serializer_class = LogoutSerializer


class UserView(APIView):
    def get(self, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data)

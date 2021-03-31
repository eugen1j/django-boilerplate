from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        try:
            # Attempt to blacklist the given refresh token
            refresh.blacklist()
        except AttributeError:
            # If blacklist app not installed, `blacklist` method will
            # not be present
            pass

        return {}

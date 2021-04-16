from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from django_boilerplate.user.models import User


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


class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'group',
            'permissions',
        ]

    def get_permissions(self, instance: User):
        return instance.group.permissions.all().values_list('codename', flat=True)

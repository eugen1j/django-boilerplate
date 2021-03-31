from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django_boilerplate.user.models import User
from django_boilerplate.user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

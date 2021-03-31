from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from django_boilerplate.user.choices import AuthGroup
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    group = models.ForeignKey(
        Group, models.PROTECT, verbose_name=_("Group"),
        related_name='users', default=AuthGroup.MANAGER)

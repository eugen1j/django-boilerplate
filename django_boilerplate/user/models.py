from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from django_boilerplate.user.permissions import AuthGroup, Permissions
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    group = models.ForeignKey(
        Group, models.PROTECT, verbose_name=_("Group"),
        related_name='users', default=AuthGroup.MANAGER)


class RightsSupport(models.Model):
    """Model for custom permissions"""

    class Meta:
        managed = False  # No database table creation or deletion  \
        # operations will be performed for this model.

        default_permissions = ()  # disable "add", "change", "delete"
        # and "view" default permissions

        permissions = Permissions.choices

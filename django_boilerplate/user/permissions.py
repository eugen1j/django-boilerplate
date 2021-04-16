from typing import Dict

from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthGroup(models.IntegerChoices):
    ADMIN = 10, _('Admin')
    MANAGER = 20, _('Manager')
    WORKER = 30, _('Worker')


class Permissions(models.TextChoices):
    MANAGE_USERS = 'MANAGE_USERS', _('Manage Users')
    VIEW_USERS = 'VIEW_USERS', _('Read Users')

    MANAGE_BLOG = 'MANAGE_BLOG', _('Manage Blog')

    MANAGE_TASKS = 'MANAGE_TASKS', _('Manage Tasks')


PERMISSION_MAP = {
    AuthGroup.ADMIN: [
        Permissions.MANAGE_USERS,
        Permissions.VIEW_USERS,
        Permissions.MANAGE_BLOG,
    ],
    AuthGroup.MANAGER: [
        Permissions.VIEW_USERS,
        Permissions.MANAGE_BLOG,
    ],
    AuthGroup.WORKER: [
        Permissions.MANAGE_TASKS,
    ],
}

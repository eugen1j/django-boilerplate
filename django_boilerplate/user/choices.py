from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthGroup(models.IntegerChoices):
    ADMIN = 10, _('Admin')
    MANAGER = 20, _('Manager')
    WORKER = 30, _('Worker')

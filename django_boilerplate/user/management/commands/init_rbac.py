from typing import Dict

from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand
from django.db import transaction

from django_boilerplate.user.permissions import AuthGroup, PERMISSION_MAP


class Command(BaseCommand):
    help = """Initialize permissions for default Groups"""

    def handle(self, *args, **options):
        with transaction.atomic():
            #  Creating groups
            groups: Dict[AuthGroup, Group] = {}
            for name, label in AuthGroup.choices:
                model, created = Group.objects.get_or_create(
                    id=name, defaults={"name": label}
                )
                groups[name] = model

            permissions: Dict[str, Permission] = {
                permission.codename: permission
                for permission in Permission.objects.all()
            }

            # Assign permissions
            for group_name, group_permissions in PERMISSION_MAP.items():
                group = groups[group_name]
                group.permissions.clear()
                for group_permission in group_permissions:
                    group.permissions.add(permissions[group_permission])

from typing import List

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from django.db import transaction

from django_boilerplate.user.choices import AuthGroup
from django_boilerplate.user.models import User
from django.utils.translation import gettext_lazy as _


class Command(BaseCommand):
    help = """Инициализация прав доступа"""

    def handle(self, *args, **options):
        with transaction.atomic():
            #  Creating groups
            admin, created = Group.objects.get_or_create(
                id=AuthGroup.ADMIN, defaults={"name": AuthGroup.ADMIN.label})
            manager, created = Group.objects.get_or_create(
                id=AuthGroup.MANAGER, defaults={"name": AuthGroup.MANAGER.label})
            worker, created = Group.objects.get_or_create(
                id=AuthGroup.WORKER, defaults={"name": AuthGroup.WORKER.label})

            # Creating perms
            admin.permissions.clear()
            manager.permissions.clear()
            worker.permissions.clear()

            # Creating new permissions
            manage_users = self.create_permission(
                User, _("Manage Users"), "manage_users")

            # Assigning permissions to groups
            self.assign_permissions([
                manage_users
            ], admin)
            self.assign_permissions([
            ], manager)
            self.assign_permissions([
            ], worker)

    def create_permission(self, model, permission_name: str, permission_codename: str):
        """Create permissions"""
        permission, created = Permission.objects.get_or_create(
            codename=permission_codename,
            content_type=ContentType.objects.get_for_model(model),
            defaults={
                "name": permission_name,
            }
        )
        return permission

    def assign_permissions(self, permissions: List[Permission], group: AuthGroup):
        """Assign permissions to group"""
        for permission in permissions:
            group.permissions.add(permission)

from rest_framework.permissions import BasePermission


def permission_builder(*permissions: str):
    class DynamicPermission(BasePermission):
        def has_permission(self, request, view):
            return bool(
                request.user and request.user.is_authenticated
                and all(request.user.has_perm(p) for p in permissions))

    return DynamicPermission

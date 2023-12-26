from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """Активность пользователя"""

    def has_permission(self, request, view):
        return request.user and request.user.is_active

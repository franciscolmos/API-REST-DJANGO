from rest_framework import permissions


class PurchasePermissions(permissions.BasePermission):
    """Solo el user R00T puede hacer compras y agregar proveedores"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser:
            return False
        return True

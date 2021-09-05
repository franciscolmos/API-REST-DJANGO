from rest_framework import permissions


class EditorPermissions(permissions.BasePermission):
    """Solo el user R00T puede crear, editar categorias"""

    def has_permission(self, request, view):
        """SOLO EL ROOT PUEDE CREAR Y MODIFICAR (CATEGORIAS Y PRODUCTOS)"""
        allowed_methods = ['POST', 'PUT', 'PATCH']
        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser and request.method in allowed_methods:
            return False
        return True

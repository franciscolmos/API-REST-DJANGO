from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """PERMITE AL USUARIO EDITAR SU PROPIO PERFIL PERO SOLO VER EL DEL RESTO"""

    def has_object_permission(self, request, view, obj):
        """Verifica si el usuario esta tratando de editar su propio perfil, caso contrario devuelve false"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
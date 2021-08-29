from rest_framework import permissions


class CategoryPermissions(permissions.BasePermission):
    """Solo el user R00T puede crear, editar categorias"""

    def has_object_permission(self, request, view, obj):
        """SOLO EL ROOT PUEDE CREAR Y MODIFICAR CATEGORIAS"""
        if request.method == 'POST':
            return True
        if request.method == 'PUT' and request.user.id == 1:
            return True
        if request.method == 'PATCH' and request.user.id == 1:
            return True
        if request.method == 'GET':
            print(request.method)
            return True
        if request.method == 'DELETE':
            if request.user.id == 1:
                return True
        return False

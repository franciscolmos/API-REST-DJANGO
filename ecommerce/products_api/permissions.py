from rest_framework import permissions


class ProductPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """SOLO EL ROOT PUEDE CREAR Y MODIFICAR PRODUCTOS"""
        print(request.method)
        if request.method == 'POST':
            if request.user.id == 1:
                return True
        if request.method == 'PUT':
            if request.user.id == 1:
                return True
        if request.method == 'PATCH':
            if request.user.id == 1:
                return True
        if request.method == 'GET':
            if request.user.id == 1:
                return True
        return True

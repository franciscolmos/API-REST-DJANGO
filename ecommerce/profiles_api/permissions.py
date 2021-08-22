# from rest_framework import permissions
#
# class UpdateOwnProfile(permissions.BasePermission):
#     """PERMITE AL USUARIO EDITAR SU PROPIO PERFIL"""
#
#     def has_object_permission(self, request, view, obj):
#         """Verifica si el usuario esta tratando de editar su propio perfil"""
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.id == request.user.id
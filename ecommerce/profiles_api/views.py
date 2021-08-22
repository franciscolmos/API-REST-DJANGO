from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from profiles_api import serializers
from profiles_api import models

class UserProfileViewSet(viewsets.ModelViewSet):
    """MANEJO DE CREADO, BORRADO Y ACTUALIZADO DE PERFILES DE USUARIO"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
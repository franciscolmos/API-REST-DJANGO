from rest_framework import viewsets
from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

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


class UserLoginApiView(ObtainAuthToken):
   """MANEJA EL CREADO DE TOKENS DE LOS USUARIOS"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
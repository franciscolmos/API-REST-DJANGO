from django.shortcuts import render
from rest_framework.views import APIVIew
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentications import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(ApiView):
    """Test API View"""
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
            'huevada 1',
            'huevada 2',
            'huevada 3',
            'huevada 4',
        ]

    class UserProfileViewSet(viewsets.ModelViewSet):
        """CONTROLADOR DE CREADO Y ACTUALIZADO DE PERFILES"""
        serializers_class = serializers.UserProfileSerializer
        queryset = models.UserProfile.objects.all()
        authentication_classes = (TokenAuthentication, )
        permissions_classes = (permissions.UpdateOwnProfile,)

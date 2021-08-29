from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from categories_api import permissions
from categories_api import serializers
from categories_api import models


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.CategoryPermissions]

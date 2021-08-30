from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from utils.permissions import EditorPermissions
from categories_api import serializers
from categories_api import models


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [EditorPermissions]

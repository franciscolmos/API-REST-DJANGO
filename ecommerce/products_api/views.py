from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from products_api import permissions
from products_api import serializers
from products_api import models


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.ProductPermissions]

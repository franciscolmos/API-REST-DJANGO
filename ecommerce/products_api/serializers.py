from rest_framework import serializers
from products_api import models


class ProductSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""

    stock = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Product
        fields = ['id', 'title', 'unitPrice', 'category', 'stock']

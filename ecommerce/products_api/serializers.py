from rest_framework import serializers
from products_api import models


class ProductSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""

    class Meta:
        model = models.Product
        fields = '__all__'

from rest_framework import serializers
from categories_api import models


class CategorySerializer(serializers.ModelSerializer):
    """Serializes a Category object"""
    category_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='categories-detail'
    )

    class Meta:
        model = models.Category
        fields = ['id', 'title', 'description', 'category_products']

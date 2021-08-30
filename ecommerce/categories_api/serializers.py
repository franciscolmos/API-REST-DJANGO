from rest_framework import serializers
from categories_api import models


class CategorySerializer(serializers.ModelSerializer):
    """Serializes a Category object"""

    class Meta:
        model = models.Category
        fields = '__all__'

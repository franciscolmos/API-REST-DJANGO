from rest_framework import serializers
from purchases_api.models import Purchase, Supplier


class PurchaseSerializer(serializers.ModelSerializer):
    """Serializes a Purchase object"""

    class Meta:
        model = Purchase
        fields = ['id', 'product', 'quantity', 'unit_price', 'supplier', 'total_price']


class SupplierSerializer(serializers.ModelSerializer):
    """Serializes a Supplier object"""

    class Meta:
        model = Supplier
        fields = ['id', 'name']

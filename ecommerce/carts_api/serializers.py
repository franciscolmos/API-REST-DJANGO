from rest_framework import serializers
from carts_api import models


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CartItem
        fields = ['product', 'cart', 'quantity', 'subtotal']


class CartSerializer(serializers.ModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='cartItems-detail'
    )

    class Meta:
        model = models.Cart
        fields = ['user', 'status', 'items', 'total']

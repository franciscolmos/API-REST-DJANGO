from rest_framework import serializers
from carts_api import models


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ['product', 'cart', 'quantity', 'subTotal']


class CartSerializer(serializers.ModelSerializer):
    cartItems = serializers.StringRelatedField(many=True)
    print("cartItems: ", cartItems)

    class Meta:
        model = models.Cart
        fields = ['user', 'status', 'cartItems']

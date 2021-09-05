from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from carts_api import serializers
from carts_api import models


class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CartSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return models.Cart.objects.all()
        return models.Cart.objects.filter(user=user)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = models.CartItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CartItemSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        print(user)
        query_param_cart = self.request.query_params.get('cart')
        print(query_param_cart)
        if user.is_superuser:
            return models.CartItem.objects.all()
        carts = models.Cart.objects.filter(user=user)
        if query_param_cart:
            carts = carts.filter(id=query_param_cart)
        if carts.last():
            return carts.last().cartItems.all()
        return self.queryset.none()

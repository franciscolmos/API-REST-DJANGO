from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from carts_api import permissions
from carts_api import serializers
from carts_api import models
from rest_framework.exceptions import PermissionDenied


class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CartSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        print("user---------------->: ", user)
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
        cart = self.request.query_params.get('cart')
        print(cart)
        if user.is_superuser:
            return models.CartItem.objects.all()
        else:
            if cart:
                if models.Cart.objects.get(id=cart).user == user:
                    return models.CartItem.objects.filter(cart__user=user)
                else:
                    raise PermissionDenied({"message": "You don't have permission to access"})
            else:
                raise PermissionDenied({"message": "please select a cart"})

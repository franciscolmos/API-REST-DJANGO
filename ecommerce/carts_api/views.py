from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from carts_api import serializers
from carts_api import models as carts_models
from products_api import models as products_models


class CartViewSet(viewsets.ModelViewSet):
    queryset = carts_models.Cart.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CartSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return carts_models.Cart.objects.all()
        return carts_models.Cart.objects.filter(user=user)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = carts_models.CartItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CartItemSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        query_param_cart = self.request.query_params.get('cart')
        print(query_param_cart)
        if user.is_superuser:
            return carts_models.CartItem.objects.all()
        carts = carts_models.Cart.objects.filter(user=user)
        if query_param_cart:
            carts = carts.filter(id=query_param_cart)
            print(carts)
        if carts.last():
            return carts.last().cartItems.all()
        return self.queryset.none()

    def create(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data['product']
        quantity = request.data['quantity']
        cart_item = carts_models.CartItem.objects.create(product=products_models.Product.objects.get(id=product_id),
                                                         quantity=quantity,
                                                         cart=carts_models.Cart.objects.get(user=user))
        return Response(status=status.HTTP_200_OK, data=request.data)

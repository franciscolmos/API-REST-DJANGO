from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from carts_api.serializers import CartItemSerializer, CartSerializer
from carts_api import models as carts_models


class CartViewSet(viewsets.ModelViewSet):
    queryset = carts_models.Cart.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return carts_models.Cart.objects.all()
        return carts_models.Cart.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        """Permite crear un nuevo carrito"""
        user = request.user
        created = carts_models.Cart.objects.create(user=user)
        created.save()
        return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Carrito creado con exito"})


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = carts_models.CartItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = CartItemSerializer
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
            return carts.last().items.all()
        return self.queryset.none()

    def create(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data['product']
        quantity = request.data['quantity']
        exist_cart = carts_models.Cart.objects.filter(user=user).last()
        """Chequeamos si existe algun carrito"""
        if not exist_cart:
            new_cart = CartViewSet(viewsets.ModelViewSet)
            CartViewSet.create(new_cart, request)
        """Chequeamos si el ultimo carrito esta cerrado"""
        last_cart_status = carts_models.Cart.get_status(exist_cart)
        if last_cart_status is True:
            new_cart = CartViewSet(viewsets.ModelViewSet)
            CartViewSet.create(new_cart, request)
        """Si el item existe le sumamos la cantidad, caso contrario se agrega nuevo item con su respectiva cantidad"""
        last_cart = carts_models.Cart.objects.filter(user=user).last()
        item, created = carts_models.CartItem.objects.get_or_create(product_id=product_id,
                                                                    cart=carts_models.Cart.objects.get(pk=last_cart.id))
        item.quantity += int(quantity)
        item.save()
        return Response(status=status.HTTP_200_OK, data=request.data)

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from carts_api.serializers import CartItemSerializer, CartSerializer
from carts_api.models import Cart, CartItem
from products_api.models import Product


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Cart.objects.all()
        return Cart.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        """Permite crear un nuevo carrito"""
        user = request.user
        created = Cart.objects.create(user=user)
        created.save()
        return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Carrito creado con exito"})

    def put(self, request):
        """Permite cerrar y comprar los items del carrito"""
        user = request.user
        last_cart = Cart.objects.filter(user=user).last()
        if last_cart.status is True:
            return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "El carrito ya se encuentra cerrado"})
        items = last_cart.items.all()
        """Se fija si los items del carrito tienen suficiente stock"""

        for item in items:
            print("item---->", item)
            product_stock = item.product.stock
            """print("item.quantity: ", item.quantity)
            print("product_stock: ", product_stock)"""
            if item.quantity > product_stock:
                print("No hay suficiente cantidad del producto ", Product.objects.get(pk=item.id).title)
                return Response(status=status.HTTP_200_OK,
                                data={"Status": "OK", "Message": "No hay stock disponible del producto"})
        """Cambia el estado del carrito para cerrarlo"""
        Cart.objects.filter(pk=last_cart.id).update(status=True)
        return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Carrito cerrado"})


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = CartItemSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        query_param_cart = self.request.query_params.get('cart')
        print(query_param_cart)
        if user.is_superuser:
            return CartItem.objects.all()
        carts = Cart.objects.filter(user=user)
        if query_param_cart:
            carts = carts.filter(id=query_param_cart)
            print(carts)
        if carts.last():
            return carts.last().items.all()
        return self.queryset.none()

    def create(self, request, *args, **kwargs):
        """Permite agregar items al carrito"""
        user = request.user
        product_id = request.data['product']
        quantity = request.data['quantity']
        exist_cart = Cart.objects.filter(user=user).last()
        """Chequeamos si existe algun carrito"""
        if not exist_cart:
            new_cart = CartViewSet(viewsets.ModelViewSet)
            CartViewSet.create(new_cart, request)
        """Chequeamos si el ultimo carrito esta cerrado"""
        last_cart_status = Cart.get_status(exist_cart)
        if last_cart_status is True:
            new_cart = CartViewSet(viewsets.ModelViewSet)
            CartViewSet.create(new_cart, request)
        """Validamos que haya stock del producto que se quiere anadir al carro"""
        product_stock = Product.objects.get(pk=product_id).stock
        if product_stock < quantity:
            return Response(status=status.HTTP_200_OK, data={"Status": "200", "Message": "No hay stock suficiente del producto para satisfacer este pedido"})
        """Si el item existe le sumamos la cantidad, caso contrario se agrega nuevo item con su respectiva cantidad"""
        last_cart = Cart.objects.filter(user=user).last()
        item, created = CartItem.objects.get_or_create(product_id=product_id,
                                                       cart=Cart.objects.get(pk=last_cart.id))
        item.quantity += int(quantity)
        item.save()
        return Response(status=status.HTTP_200_OK, data=request.data)

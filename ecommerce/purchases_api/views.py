from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from purchases_api.permissions import PurchasePermissions
from purchases_api.serializers import PurchaseSerializer, SupplierSerializer
from products_api.models import Product
from purchases_api.models import Purchase, Supplier


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [PurchasePermissions]

    def create(self, request, *args, **kwargs):
        """Permite Realizar una compra de un producto a un proveedor"""
        product_id = request.data['product']
        quantity = request.data['quantity']
        purchase_price = request.data['purchase_price']
        supplier = request.data['supplier']
        """Buscamos el producto y el proveedor que pasamos por body"""
        exist_product = Product.objects.filter(pk=product_id)
        exist_supplier = Supplier.objects.filter(pk=supplier)
        """Verificamos que el producto exista, caso contratrio no se concreta la venta"""
        if not exist_product:
            return Response(status=status.HTTP_200_OK, data={"status": "OK", "Message": "Ese producto no existe en inventario"})
        """Verificamos que el proveedor exista, caso contrario no se concreta la venta"""
        if not exist_supplier:
            return Response(status=status.HTTP_200_OK, data={"status": "OK", "Message": "El proveedor no existe"})
        """Si las verificaciones dan Ok, se crea el purchase"""
        product = Product.objects.get(pk=product_id)
        supplier = Supplier.objects.get(pk=supplier)
        """Creamos un objeto del tipo Purchase, para poder hacerle save()"""
        new_purchase = Purchase()
        new_purchase.product = product
        new_purchase.quantity = quantity
        new_purchase.purchase_price = purchase_price
        new_purchase.supplier = supplier
        new_purchase.save()
        return Response(status=status.HTTP_200_OK, data=request.data)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = SupplierSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [PurchasePermissions]

    def get_queryset(self):
        """Listamos todos los proveedores cargados"""
        return Supplier.objects.all()

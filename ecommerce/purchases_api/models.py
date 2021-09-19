from django.db import models
from products_api.models import Product


class Supplier(models.Model):
    """Modelo de proveedor"""
    name = models.TextField(max_length=255, default="test supplier")


class Purchase(models.Model):
    """Modelo utilizado para realizar compras de productos y aumentar el stock"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.SmallIntegerField(default=0)
    purchase_price = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='category_products')

    @property
    def total_price(self):
        return self.purchase_price * self.quantity


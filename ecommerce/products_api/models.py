from django.db import models
from categories_api.models import Category


class Product(models.Model):
    title = models.TextField(max_length=255, default="test product")
    unitPrice = models.FloatField(default=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')

    @property
    def stock(self):
        sales = self.sales.filter(cart__status=True).aggregate(total=models.Sum('quantity')).get('total')
        sales = 0 if not sales else sales
        purchases = self.purchases.aggregate(total=models.Sum('quantity')).get('total')
        purchases = 0 if not purchases else purchases
        print("purchases - sales: ", purchases - sales)
        return purchases - sales

    def __str__(self):
        return self.title


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.SmallIntegerField(default=0)
    unit_price = models.FloatField(default=0)


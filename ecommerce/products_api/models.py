from django.db import models
from categories_api import models as models1


class Product(models.Model):
    title = models.TextField(max_length=255, default="test product")
    unitPrice = models.FloatField()
    category = models.ForeignKey(models1.Category, on_delete=models.CASCADE, related_name='category_products')

    def __str__(self):
        return self.title

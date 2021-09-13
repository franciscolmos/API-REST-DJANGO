from django.db import models
from profiles_api import models as userProfileModel
from products_api import models as productModel


class Cart(models.Model):
    user = models.ForeignKey(userProfileModel.UserProfile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    @property
    def total(self):
        total = 0
        for itemCart in self.items.all():
            total += itemCart.subtotal
        return total

    def __str__(self):
        return "{} ({})".format("Carrito de compras de ", self.user.email, self.status)


class CartItem(models.Model):
    product = models.ForeignKey(productModel.Product, on_delete=models.CASCADE, related_name='sales')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', default=0)
    quantity = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.product.unitPrice * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'title: {self.product.title} ' \
               f'quantity: {self.quantity} ' \
               f'sub_total: {self.subtotal} '

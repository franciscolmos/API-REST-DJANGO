from django.db import models
from profiles_api import models as userProfileModel
from products_api import models as productModel


class Cart(models.Model):
    user = models.ForeignKey(userProfileModel.UserProfile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.user.email, self.status)

    @property
    def total(self):
        total = 0
        for itemCart in CartItem.objects.filter(cart=self):
            total += itemCart.price * itemCart.amount
        return total


class CartItem(models.Model):
    product = models.ForeignKey(productModel.Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartItems')
    quantity = models.IntegerField()
    subTotal = models.FloatField()

    def __str__(self):
        return f'title: {self.product.title} ' \
               f'quantity: {self.quantity} ' \
               f'subTotal: {self.subTotal} '
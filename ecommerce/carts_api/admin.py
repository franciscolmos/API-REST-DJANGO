from django.contrib import admin
from carts_api import models

admin.site.register(models.Cart)
admin.site.register(models.CartItem)

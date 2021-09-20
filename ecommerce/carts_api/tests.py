from django.test import TestCase, Client
import json

from profiles_api.models import UserProfile
from carts_api.models import Cart, CartItem
from products_api.models import Product
from categories_api.models import Category
from purchases_api.models import Purchase, Supplier


class ProductTest(TestCase):

    def setUp(self):
        self.browser = Client()
        """Creamos un usuario para hacer compras en un carrito"""
        self.test_user = UserProfile.objects.create(email='test@test.test',
                                                    name='test',
                                                    is_active=True,
                                                    is_staff=False)
        self.test_user.set_password('test_test')
        self.test_user.save()

        """Creamos un usuario root para comprar stock"""
        self.test_root = UserProfile.objects.create(email='root@root.root',
                                                    name='root',
                                                    is_active=True,
                                                    is_staff=True)
        self.test_root.set_password('root_root')
        self.test_root.save()

        """Creamos una categoria de test"""
        self.category1 = Category.objects.create()

        """Agregamos dos productos a la categoria anterior"""
        self.producto_1 = Product.objects.create(title='Space Captain', unitPrice=100, category=self.category1)
        self.producto_2 = Product.objects.create(category=self.category1)

        """Creamos un Proveedor"""
        self.supplier = Supplier.objects.create(name='The Big Seven')

        """Agregamos stock de los productos anteriormente creados"""
        self.purchase = Purchase.objects.create(product=self.producto_2, quantity=50, purchase_price=1500, supplier=self.supplier)
        self.purchase = Purchase.objects.create(product=self.producto_1, quantity=25, purchase_price=25, supplier=self.supplier)

        """Creamos un carrito de compras que vamos a testear"""
        self.shop_cart = Cart.objects.create(user=self.test_user)

        """Agregamos un item al carrito"""
        self.shop_cart_item = CartItem.objects.create(product=self.producto_1, cart=self.shop_cart, quantity=2)

        response = self.browser.post('/api/login/', {'username': 'test@test.test', 'password': 'test_test'})
        token = "Token " + json.loads(response.content)['token']
        self.browser.defaults['HTTP_AUTHORIZATION'] = token

    def test_shop_cart(self):
        """Verificamos que se calcule bien el total del carrito al agregar items al mismo"""
        self.assertEqual(self.shop_cart.total, 200)
        added_prod = dict(product=self.producto_2.id, quantity=2)
        self.browser.post('/api/cartItems/', json.dumps(added_prod), content_type="application/json")
        self.assertEqual(self.shop_cart.total, 2200)

    def test_product_stock(self):
        """Verificamos que se calcule bien el stock del producto cuando compramos y vendemos"""
        self.assertEqual(self.producto_1.stock, 25)
        self.assertEqual(self.producto_2.stock, 50)
        """Corremos el test test_shop_cart para que reflejen las compras del producto_2"""
        self.test_shop_cart()
        """Cerramos el carrito de compras para que se actualiza el stock"""
        self.browser.put('/api/carts/', content_type="application/json")
        self.assertEqual(self.producto_1.stock, 23)
        self.assertEqual(self.producto_2.stock, 48)

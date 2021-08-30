from rest_framework.routers import DefaultRouter
from carts_api import views

router = DefaultRouter()
router.register('carts', views.CartViewSet, basename="carts")
router.register('cartItems', views.CartItemViewSet, basename="cartItems")

urlpatterns = router.urls
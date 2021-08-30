from rest_framework.routers import DefaultRouter
from products_api import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename="products")

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from purchases_api.views import PurchaseViewSet, SupplierViewSet

router = DefaultRouter()
router.register('purchase', PurchaseViewSet, basename="purchase")
router.register('supplier', SupplierViewSet, basename="supplier")

urlpatterns = router.urls
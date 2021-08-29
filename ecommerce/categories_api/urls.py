from rest_framework.routers import DefaultRouter
from categories_api import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename="categories")

urlpatterns = router.urls

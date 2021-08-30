from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginApiView, UserProfileViewSet, UserProfileFeedViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet, basename="profiles")
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
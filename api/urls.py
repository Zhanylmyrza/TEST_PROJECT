from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, ProfileViewSet, home



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

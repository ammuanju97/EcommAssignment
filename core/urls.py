from django.urls import include, path
from rest_framework import routers
from .views import CustomerViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

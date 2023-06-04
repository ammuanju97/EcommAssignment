from rest_framework import viewsets, mixins
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['put'])
    def toggle_activation(self, request, pk=None):
        product = self.get_object()
        registered_months_ago = (timezone.now().date() - product.created_at).days // 30
        if registered_months_ago >= 2:
            product.is_active = not product.is_active
            product.save()
            return Response({'message': 'Product activation status toggled.'})
        return Response({'message': 'Product cannot be deactivated yet.'})

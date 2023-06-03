from rest_framework.viewsets import ModelViewSet
from store.models import *
from .serializers import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
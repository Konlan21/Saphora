from rest_framework.serializers import ModelSerializer
from store.models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']

class CollectionSerializer(ModelSerializer):
    model = Collection
    fields = ['id', 'title']


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email']


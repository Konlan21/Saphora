from rest_framework.serializers import ModelSerializer
from store.models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'digital', 'description']


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'date_ordered', 'transaction_id', 'payment_status']
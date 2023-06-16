from rest_framework.serializers import ModelSerializer
from store.models import *
from rest_framework import serializers


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
    customer = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = ['id', 'customer', 'date_ordered', 'transaction_id', 'payment_status']

class OrderItemSerializer(ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', 'quantity', 'date_added']


class ShippingAddressSerializer(ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = ShippingAddress
        fields = ['customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added']

    
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['name', 'description', 'date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Reviews.objects.create(product_id=product_id, **validated_data)
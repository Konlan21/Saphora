from django.contrib import admin
from store.models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'user'] 
    list_filter = ['email']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'inventory', 'digital']
    # list_editable = ['name', 'price', 'digital']
    list_filter = ['price']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'completed', 'transaction_id', 'payment_status']
    list_filter = ['date_ordered']
    search_fields = ['customer']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'date_added']
    list_per_page = 10


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'state', 'zipcode', 'date_added']
    list_filter = ['address']
    search_fields = ['address']
    list_per_page = 10


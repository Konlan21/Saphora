from django.contrib import admin
from store.models import *
from django.db.models.aggregates import Count


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'user'] 
    list_filter = ['email']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Collection)
class Collection(admin.ModelAdmin):
    list_display = ['id', 'title', 'products_count']
    list_per_page = 10

    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'inventory_status', 'digital']
    list_filter = ['price']
    list_per_page = 10
    search_fields = ['name']

    def inventory_status(self, product):
            if product.inventory < 10:
                return "Low"
            return "Ok"


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

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['product', 'description', 'name', 'date']
    list_filter = ['product']
    search_fields = ['description', 'name']
import imp
from itertools import product
from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html
from django.urls import reverse
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title',
                    'collection', 'inventory_status']
    list_filter = ['last_update']
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title']
    list_filter = ['collection', 'last_update']

    @admin.display(ordering='inventory_status')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'High'

    def collection(self, product):
        product.collection


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ['id', 'payment_status']
    list_editable = ['payment_status']
    list_per_page = 15
    list_select_related = ['customer']


@ admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'products_count']
    list_filter = ['title', 'id']

    @ admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

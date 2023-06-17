from django.urls import path
from rest_framework_nested import routers
from .views import *



router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products_list')
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
router.register('customers', CustomerViewSet)
router.register('collections', CollectionViewSet)
router.register('orders', OrderViewset)
router.register('order_items', OrderItemViewSet)
router.register('shipping_address', ShippingAddressViewSet)
urlpatterns = router.urls + products_router.urls 
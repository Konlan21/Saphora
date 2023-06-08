from django.urls import path
from rest_framework_nested import routers
from .views import *



router = routers.DefaultRouter()
router.register('products', ProductViewSet)
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
router.register('customers', CustomerViewSet, basename='customer-list')
router.register('collections', CollectionViewSet, basename='customer-list')
router.register('orders', OrderViewset, basename='order-list')

urlpatterns = router.urls + products_router.urls 
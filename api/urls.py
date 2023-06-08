from django.urls import path
from rest_framework_nested import routers
from .views import *



router = routers.DefaultRouter()
router.register('product_list', ProductViewSet)
products_router = routers.NestedDefaultRouter(router, 'product_list', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
router.register('customer_list', CustomerViewSet)
router.register('collection_list', CollectionViewSet)
router.register('order_list', OrderViewset)

urlpatterns = router.urls + products_router.urls
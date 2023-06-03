from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()
router.register('product_list', ProductViewSet)
router.register('customer_list', CustomerViewSet)
router.register('collection_list', CollectionViewSet)

urlpatterns = router.urls
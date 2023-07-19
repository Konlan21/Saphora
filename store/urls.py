from django.urls import path
from . import views



urlpatterns = [  
    path('', views.store, name='store'),
    path('store/<int:id>/', views.product_detail, name='product-detail'),
    path('search_product/', views.search_products, name='search-products'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order')  
]  
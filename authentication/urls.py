from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_customer, name='customer-login'),
    path('logout/', views.logout_customer, name='customer-logout'),
    path('signup/', views.register_customers, name='customer-signup')
]
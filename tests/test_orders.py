from rest_framework.test import APIClient
from rest_framework import status 
from django.contrib.auth.models import User 
import pytest


@pytest.mark.django_db
class TestCreateOrder:
    def test_if_user_not_autheticated_returns_403(self):
        client = APIClient()
        response = client.post('http://localhost:8000/api/orders/', {'id': 90})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_authenticate_returns_201(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('http://localhost:8000/api/orders/', {'id': 367})
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_orders_returns_201(self):
        client = APIClient()
        response = client.get('http://localhost:8000/api/orders/')
        assert response.status_code == status.HTTP_200_OK
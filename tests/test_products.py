from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User



class TestCreateProducts:
    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        response = client.post('http://localhost:8000/api/products/', {'name': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('http://localhost:8000/api/products/', {'name': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST



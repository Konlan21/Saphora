from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_admin_returns_403(self):
        client = APIClient()
        response = client.post('http://localhost:8000/api/collections/', {'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
from rest_framework.test import APIClient  
from rest_framework import status



class TestCustomerCreation:
    def test_if_user_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('http://127.0.0.1:8000/api/customer_list/', {'first_name': 'ee'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
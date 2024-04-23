import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


@pytest.fixture
def api_client():
    return APIClient()


class Oauth2ProvideJWTTokenPOSTTests(APITestCase):
    def setUp(self):
        self.api_url = reverse("oauth2_provider_jwt:token")

    def test_token_view_post(self):
        data = {
            "grant_type": "your_grant_type",
        }
        response = self.client.post(self.api_url, data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

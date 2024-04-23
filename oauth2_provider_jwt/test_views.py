import pytest
import json
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

    def test_post_invalid_grant_type(self):
        data = {
            "grant_type": "invalid_grant_type",
        }
        response = self.client.post(self.api_url, data=json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"error": "unsupported_grant_type"})

    def test_post_invalid_client(self):
        data = {"grant_type": "client_credentials"}
        response = self.client.post(self.api_url, data=json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {"error": "invalid_client"})

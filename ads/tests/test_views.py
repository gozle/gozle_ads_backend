from django.urls import reverse

from rest_framework import test

from ads.serializers import BannerSerializer, ImputSerializer
from helpers.base64_test_image import TEST_IMAGE_BASE64
from helpers.tests import create_banner, create_imput


class BannerViewsTestCase(test.APITestCase):
    client = test.APIClient()
    data = {
        "text": "Gozle Portal",
        "description": "Market where you can buy computer games and apps",
        "link": "https://store.gozle.com.tm/",
        "image": TEST_IMAGE_BASE64,
    }
    url = reverse("banner-list")

    def test_banner_queryset(self):
        banner_1 = create_banner()
        banner_2 = create_banner()
        response = self.client.get(self.url)
        serializer_data = BannerSerializer(
            [banner_1, banner_2], many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer_data)

    def test_banner_post(self):
        self.data["age_from"] = None
        self.data["age_to"] = None
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 201)

    def test_banner_wrong_from_age(self):
        self.data["age_from"] = 18
        self.data["age_to"] = 6
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 400)

    def test_banner_age_max_validator(self):
        self.data["age_from"] = 100
        self.data["age_to"] = 100
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 400)

    def test_banner_age_equality_wrong(self):
        self.data["age_from"] = 18
        self.data["age_to"] = 18
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 400)


class ImputViewsTestCase(test.APITestCase):
    client = test.APIClient()
    data = {
        "link": "https://store.gozle.com.tm/",
        "image": TEST_IMAGE_BASE64,
    }
    url = reverse("imput-list")

    def test_imput_queryset(self):
        imput_1 = create_imput()
        imput_2 = create_imput()
        response = self.client.get(self.url)
        serializer_data = ImputSerializer(
            [imput_1, imput_2], many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer_data)

    def test_imput_post(self):
        self.data["age_from"] = None
        self.data["age_to"] = None
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 201)

    def test_imput_wrong_from_age(self):
        self.data["age_from"] = 18
        self.data["age_to"] = 6
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 400)

    def test_imput_age_max_validator(self):
        self.data["age_from"] = 100
        self.data["age_to"] = 100
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 400)

    def test_imput_age_equality_wrong(self):
        self.data["age_from"] = 18
        self.data["age_to"] = 18
        request = self.client.post(self.url, self.data, format="json")
        self.assertEqual(request.status_code, 400)

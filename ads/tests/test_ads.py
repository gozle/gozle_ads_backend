from django.urls import reverse

from rest_framework import test

from ads.serializers import BannerAdsSerializer, ImputAdsSerializer, VideoAdsSerializer
from helpers.tests import create_banner, create_imput


class BannerAdsTestCase(test.APITestCase):
    client = test.APIClient()
    url = reverse("banner-ads")

    def test_banner_ads_views_status_code(self):
        # Test Status code 204
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 204)
        # Test Status code 200
        create_banner()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_banner_ads_queryset(self):
        banner = create_banner()
        response_data = self.client.get(self.url).data
        serializer_data = BannerAdsSerializer(banner).data
        self.assertEqual(response_data, serializer_data)


class ImputAdsTestCase(test.APITestCase):
    client = test.APIClient()
    url = reverse("imput-ads")

    def test_imput_ads_views_status_code(self):
        # Test Status code 204
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 204)
        # Test Status code 200
        create_imput()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_imput_ads_queryset(self):
        imput = create_imput()
        response_data = self.client.get(self.url).data
        serializer_data = ImputAdsSerializer(imput).data
        self.assertEqual(response_data, serializer_data)

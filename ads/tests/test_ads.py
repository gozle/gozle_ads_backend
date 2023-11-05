from django.core.cache import cache
from django.urls import reverse
from rest_framework import test

from ads.serializers import BannerSerializer, ImputSerializer
from helpers.tests import create_banner, create_imput


class BannerAdsTestCase(test.APITestCase):
    client = test.APIClient()
    url = reverse("banner-ads")
    cache.clear()

    def test_banner_ads_views_status_code_204(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 204)
    
    def test_banner_ads_views_status_code_200(self):
        create_banner()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_banner_ads_queryset(self):
        banner = create_banner()
        response_data = self.client.get(self.url).data
        serializer_data = BannerSerializer(banner).data
        response_data["view_count"] = serializer_data["view_count"]

        self.assertEqual(response_data, serializer_data)

    def test_banner_view_count_increasing(self):
        banner = create_banner()
        banner_view_count_before = banner.view_count
        response_data = self.client.get(self.url).data
        banner_view_count_after = response_data["view_count"]

        self.assertLess(banner_view_count_before, banner_view_count_after)

    def test_banner_changing_by_less_view_count(self):
        create_banner(), create_banner()
        response_data = self.client.get(self.url).data
        banner_id_1 = response_data["id"]
        response_data = self.client.get(self.url).data
        banner_id_2 = response_data["id"]

        self.assertNotEqual(banner_id_1, banner_id_2)


class ImputAdsTestCase(test.APITestCase):
    client = test.APIClient()
    url = reverse("imput-ads")
    cache.clear()

    def test_imput_ads_views_status_code_204(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 204)

    def test_imput_ads_views_status_code_200(self):

        create_imput()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_imput_ads_queryset(self):
        imput = create_imput()
        response_data = self.client.get(self.url).data
        serializer_data = ImputSerializer(imput).data
        response_data["view_count"] = serializer_data["view_count"]
        self.assertEqual(response_data, serializer_data)

    def test_imput_view_count_increasing(self):
        imput = create_imput()
        imput_view_count_before = imput.view_count
        response_data = self.client.get(self.url).data
        imput_view_count_after = response_data["view_count"]

        self.assertLess(imput_view_count_before, imput_view_count_after)

    def test_imput_changing_by_less_view_count(self):
        create_imput(), create_imput()
        response_data = self.client.get(self.url).data
        imput_id_1 = response_data["id"]
        response_data = self.client.get(self.url).data
        imput_id_2 = response_data["id"]

        self.assertNotEqual(imput_id_1, imput_id_2)

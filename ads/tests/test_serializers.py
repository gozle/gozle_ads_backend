from django.urls import reverse

from rest_framework import test

from ads.models import Banner
from ads.serializers import BannerSerializer, BannerAdsSerializer
from helpers.tests import create_banner, banner_model


class BannerSerializerTestCase(test.APITestCase):
    client = test.APIClient()

    def test_banner_serializer_status_code_200(self):
        self.banner = create_banner()
        self.url = reverse("banner-ads")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_banner_serializer_status_code_204(self):
        self.url = reverse("banner-ads")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 204)

    # def test_banner_age_limit(self):
    #     data = Banner(text="Gozle Portal", description="Market where you can buy computer games and apps",
    #                   link="https://store.gozle.com.tm/", age_from=12, age_to=123)
    #     print(data)
    #     self.banner = banner_model()
    #     serializer = BannerSerializer(data=data)
    #     print(serializer.is_valid())
    #     self.assertFalse(serializer.is_valid())

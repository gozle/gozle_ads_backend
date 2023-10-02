from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer

from .models import Banner, Imput, Video


class BannerSerializer(ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Banner
        fields = ["id", "text", "description", "image", "link"]


class ImputSerializer(ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Imput
        fields = ["id", "image", "link"]


class VideoSerializer(ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Video
        fields = ["id", "image", "link"]

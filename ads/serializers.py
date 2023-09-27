from rest_framework.serializers import ModelSerializer

from .models import Banner, Imput, Video


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class ImputSerializer(ModelSerializer):
    class Meta:
        model = Imput
        fields = "__all__"


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

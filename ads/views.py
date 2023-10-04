from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    BannerSerializer,
    ImputSerializer,
    VideoSerializer,
    BannerAdsSerializer,
    ImputAdsSerializer,
    VideoAdsSerializer
)
from .models import Banner, Imput, Video
from helpers.views import ads_data


class BannerViewSet(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class BannerDetailAPIView(APIView):
    """Banner getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return BannerSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Banner, BannerAdsSerializer)


class ImputViewSet(ModelViewSet):
    serializer_class = ImputSerializer
    queryset = Imput.objects.all()


class ImputDetailAPIView(APIView):
    """Imput getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return ImputSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Imput, ImputAdsSerializer)


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class VideoDetailAPIView(APIView):
    """Video getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return VideoSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Video, VideoAdsSerializer)

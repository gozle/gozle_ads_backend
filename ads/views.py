from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    BannerSerializer,
    DeviceSerializer,
    ImputSerializer,
    VideoSerializer,
)
from .models import Banner, Device, Imput, Video
from helpers.views import ads_data


class DeviceViewSet(ModelViewSet):
    model = Device
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return self.model.objects.all()


class BannerViewSet(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().prefetch_related("devices")


class BannerDetailAPIView(APIView):
    """Banner getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return BannerSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Banner, BannerSerializer)


class ImputViewSet(ModelViewSet):
    serializer_class = ImputSerializer
    queryset = Imput.objects.all().prefetch_related("devices")


class ImputDetailAPIView(APIView):
    """Imput getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return ImputSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Imput, ImputSerializer)


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all().prefetch_related("devices")


class VideoDetailAPIView(APIView):
    """Video getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return VideoSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Video, VideoSerializer)

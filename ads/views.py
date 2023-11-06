from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from helpers.mixins import TaskCreatorMixin
from helpers.utils import ads_data

from .models import Banner, Device, Imput, Video
from .serializers import (BannerSerializer, DeviceSerializer, ImputSerializer,
                          VideoSerializer)


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class BannerViewSet(TaskCreatorMixin, ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().prefetch_related("devices")
    ads_type = "banner"


class BannerAdsAPIView(APIView):
    """Banner getter by less view count (temporary)"""

    def get_serializer(self, *args, **kwargs):
        return BannerSerializer(*args, **kwargs)

    def get(self, request):
        data = ads_data(Banner, BannerSerializer)
        if data:
            return Response(data, 200)
        return Response({"message": "There is no banner ads"})


class ImputViewSet(TaskCreatorMixin, ModelViewSet):
    serializer_class = ImputSerializer
    queryset = Imput.objects.all().prefetch_related("devices")
    ads_type = "imput"


class ImputAdsAPIView(APIView):
    """Imput getter by less view count (temporary)"""

    def get_serializer(self, *args, **kwargs):
        return ImputSerializer(*args, **kwargs)

    def get(self, request):
        data = ads_data(Imput, ImputSerializer)
        if data:
            return Response(data, 200)
        return Response({"message": "There is no imput ads"})


class VideoViewSet(TaskCreatorMixin, ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all().prefetch_related("devices")
    ads_type = "video"


class VideoAdsAPIView(APIView):
    """Video getter by less view count (temporary)"""

    def get_serializer(self, *args, **kwargs):
        return VideoSerializer(*args, **kwargs)

    def get(self, request):
        data = ads_data(Video, VideoSerializer)
        if data:
            return Response(data, 200)
        return Response({"message": "There is no video ads"})

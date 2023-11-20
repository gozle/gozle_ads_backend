from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from helpers.utils import ads_data

from .filters import BannerFilterSet, ImputFilterSet, VideoFilterSet
from .models import Banner, Device, Imput, Video
from .pagination import AdsPagination
from .serializers import (BannerSerializer, DeviceSerializer, ImputSerializer,
                          VideoSerializer)


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class BannerViewSet(ModelViewSet):
    queryset = (Banner.objects.all()
                .prefetch_related("devices")
                .prefetch_related("provinces"))
    serializer_class = BannerSerializer
    pagination_class = AdsPagination
    ads_type = "banner"


class BannerAdsAPIView(APIView):
    """Banner getter by less view count"""
    queryset = (Banner.objects.active_advertisements()
                .prefetch_related("devices")
                .prefetch_related("provinces"))

    def get_serializer(self, *args, **kwargs):
        return BannerSerializer(*args, **kwargs)

    def get(self, request):
        qs = BannerFilterSet(request.GET, self.queryset).qs
        qs_count = qs.count()
        if qs_count != 0:
            data = ads_data(qs, qs_count, BannerSerializer)
            return Response(data)

        return Response({"message": "There is no banner ads"}, status=204)


class ImputViewSet(ModelViewSet):
    queryset = (Imput.objects.all()
                .prefetch_related("devices")
                .prefetch_related("provinces"))
    serializer_class = ImputSerializer
    pagination_class = AdsPagination
    ads_type = "imput"


class ImputAdsAPIView(APIView):
    """Imput getter by less view count"""
    queryset = (Imput.objects.active_advertisements()
                .prefetch_related("devices")
                .prefetch_related("provinces"))

    def get_serializer(self, *args, **kwargs):
        return ImputSerializer(*args, **kwargs)

    def get(self, request):
        qs = ImputFilterSet(request.GET, self.queryset).qs
        qs_count = qs.count()
        if qs_count != 0:
            data = ads_data(qs, qs_count, ImputSerializer)
            return Response(data)
        return Response({"message": "There is no imput ads"}, status=204)


class VideoViewSet(ModelViewSet):
    queryset = (Video.objects.all()
                .prefetch_related("devices")
                .prefetch_related("provinces"))
    serializer_class = VideoSerializer
    pagination_class = AdsPagination
    ads_type = "video"


class VideoAdsAPIView(APIView):
    """Video getter by less view count"""
    queryset = (Video.objects.active_advertisements()
                .prefetch_related("devices")
                .prefetch_related("provinces"))

    def get_serializer(self, *args, **kwargs):
        return VideoSerializer(*args, **kwargs)

    def get(self, request):
        qs = VideoFilterSet(request.GET, self.queryset).qs
        qs_count = qs.count()
        if qs_count != 0:
            data = ads_data(qs, qs_count, VideoSerializer)
            return Response(data)
        return Response({"message": "There is no video ads"}, status=204)

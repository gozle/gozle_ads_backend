from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    BannerSerializer,
    ImputSerializer,
    VideoSerializer
)
from .models import Banner, Imput, Video


class BannerViewSet(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class BannerDetailAPIView(APIView):
    """Banner getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return BannerSerializer(*args, **kwargs)

    def get(self, request):
        banner_count = Banner.objects.all().count()
        if banner_count != 0:
            queryset = Banner.objects.all().order_by("view_count")[0]
            serializer = BannerSerializer(queryset)
            queryset.count_increase()
            return Response(serializer.data)

        return Response(status=404)


class ImputViewSet(ModelViewSet):
    serializer_class = ImputSerializer
    queryset = Imput.objects.all()


class ImputDetailAPIView(APIView):
    """Imput getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return ImputSerializer(*args, **kwargs)

    def get(self, request):
        imput_count = Imput.objects.all().count()
        if imput_count != 0:
            queryset = Imput.objects.all().order_by("view_count")[0]
            serializer = ImputSerializer(queryset)
            queryset.count_increase()
            return Response(serializer.data)

        return Response(status=404)


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class VideoDetailAPIView(APIView):
    """Video getter by less view count"""

    def get_serializer(self, *args, **kwargs):
        return VideoSerializer(*args, **kwargs)

    def get(self, request):
        video_count = Video.objects.all().count()
        if video_count != 0:
            queryset = Video.objects.all().order_by("view_count")[0]
            serializer = VideoSerializer(queryset)
            queryset.count_increase()
            return Response(serializer.data)

        return Response(status=404)

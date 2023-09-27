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


class ImputViewSet(ModelViewSet):
    serializer_class = ImputSerializer
    queryset = Imput.objects.all()


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

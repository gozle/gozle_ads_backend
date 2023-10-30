from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    BannerSerializer,
    DeviceSerializer,
    ImputSerializer,
    VideoSerializer,
)
from .models import (
    Banner,
    Device,
    Imput,
    Video
)
from helpers.utils import (
    ads_data,
    create_clock_schedule,
    create_status_hide_task,
    HIDE_TASK_NAMES
)


class TaskCreatorMixin:

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        duration = response.data["duration"]
        uuid = response.data["uuid"]
        # Creating Celery task which hide object's status to hidden
        schedule = create_clock_schedule(duration=duration)
        task = create_status_hide_task(
            schedule=schedule,
            uuid=uuid,
            task_name=self.adv_type["banner"]
        )
        return response


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class BannerViewSet(TaskCreatorMixin, ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().prefetch_related("devices")
    adv_type = "banner"


class BannerAdsAPIView(APIView):
    """Banner getter by less view count (temporary)"""

    def get_serializer(self, *args, **kwargs):
        return BannerSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Banner, BannerSerializer)


class ImputViewSet(TaskCreatorMixin, ModelViewSet):
    serializer_class = ImputSerializer
    queryset = Imput.objects.all().prefetch_related("devices")
    adv_type = "imput"


class ImputAdsAPIView(APIView):
    """Imput getter by less view count (temporary)"""

    def get_serializer(self, *args, **kwargs):
        return ImputSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Imput, ImputSerializer)


class VideoViewSet(TaskCreatorMixin, ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all().prefetch_related("devices")
    adv_type = "video"


class VideoAdsAPIView(APIView):
    """Video getter by less view count (temporary)"""

    def get_serializer(self, *args, **kwargs):
        return VideoSerializer(*args, **kwargs)

    def get(self, request):
        return ads_data(Video, VideoSerializer)

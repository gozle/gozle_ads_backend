from rest_framework.viewsets import ModelViewSet

from .models import Device
from .serializers import DeviceSerializer


class DeviceViewSet(ModelViewSet):
    model = Device
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return self.model.objects.all()

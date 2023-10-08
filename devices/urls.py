from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import DeviceViewSet

urlpatterns = [

]

router = SimpleRouter()
router.register("devices", DeviceViewSet, basename="devices")

urlpatterns += router.urls

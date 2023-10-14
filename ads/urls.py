from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path("banner/ads/", views.BannerAdsAPIView.as_view(), name="banner-ads"),
    path("imput/ads/", views.ImputAdsAPIView.as_view(), name="imput-ads"),
    path("video/ads/", views.VideoAdsAPIView.as_view(), name="video-ads"),
]


router = SimpleRouter()
router.register("banner", views.BannerViewSet, basename="banner")
router.register("imput", views.ImputViewSet, basename="imput")
router.register("video", views.VideoViewSet, basename="video")
router.register("devices", views.DeviceViewSet, basename="devices")

urlpatterns += router.urls

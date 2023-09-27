from rest_framework.routers import SimpleRouter

from .views import (
    BannerViewSet,
    ImputViewSet,
    VideoViewSet
)

router = SimpleRouter()
router.register("banner", BannerViewSet, basename="banner")
router.register("imput", ImputViewSet, basename="imput")
router.register("video", VideoViewSet, basename="video")

urlpatterns = router.urls

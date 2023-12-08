from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CityViewSet, ProvinceViewSet

urlpatterns = [
    
]

router = SimpleRouter()

router.register("cities", CityViewSet, basename="city")
router.register("provinces", ProvinceViewSet, basename="province")

urlpatterns += router.urls

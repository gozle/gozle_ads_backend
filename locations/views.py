from rest_framework.viewsets import ModelViewSet

from helpers.permissions import IsAdminOrReadOnly

from .filters import CityFilterSet
from .models import City, Province
from .serializers import CitySerializer, ProvinceSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilterSet
    permission_classes = (IsAdminOrReadOnly, )


class ProvinceViewSet(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = (IsAdminOrReadOnly, )

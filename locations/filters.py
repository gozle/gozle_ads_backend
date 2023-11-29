from django_filters import CharFilter, FilterSet

from .models import City


class CityFilterSet(FilterSet):
    province = CharFilter(field_name='province__id')

    class Meta:
        model = City
        fields = ['province']

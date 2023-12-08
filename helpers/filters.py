from django.db.models import Q
from django_filters import ChoiceFilter, FilterSet, NumberFilter, ModelMultipleChoiceFilter
from django.utils import timezone

from ads.models import AdvertisementModelMixin, Device
from locations.models import City, Province


class AdvertisementFilterSetMixin(FilterSet):
    language = ChoiceFilter(
        field_name='language',
        lookup_expr='exact',
        choices=AdvertisementModelMixin.Languages.choices
    )
    birth_year = NumberFilter(
        label="User birth year",
        field_name='birth_year',
        method='filter_birth_year'
    )
    cities = ModelMultipleChoiceFilter(
        field_name='cities',
        to_field_name='id',
        queryset=City.objects.all(),
    )
    provinces = ModelMultipleChoiceFilter(
        field_name='provinces',
        to_field_name='id',
        queryset=Province.objects.all(),
    )
    devices = ModelMultipleChoiceFilter(
        field_name='devices',
        to_field_name='id',
        queryset=Device.objects.all(),
    )

    def filter_birth_year(self, queryset, name, value):
        current_year = timezone.now().year
        age = current_year - value
        return queryset.filter(
            Q(min_age=None) | Q(min_age__lte=age),
            Q(max_age=None) | Q(max_age__gte=age),
        )

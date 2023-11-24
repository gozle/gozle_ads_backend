from django.db.models import Q
from django_filters import FilterSet, NumberFilter, ModelMultipleChoiceFilter

from ads.models import Device
from locations.models import City, Province


class AdvertisementFilterSetMixin(FilterSet):
    user_age = NumberFilter(label="User age", field_name='user_age', method='filter_user_age')
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

    def filter_user_age(self, queryset, name, value):
        return queryset.filter(
            Q(min_age=None) | Q(min_age__lte=value),
            Q(max_age=None) | Q(max_age__gte=value),
        )

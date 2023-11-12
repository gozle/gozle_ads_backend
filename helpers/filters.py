from django.db.models import Q
from django_filters import FilterSet, NumberFilter


class AdvertisementFilterSetMixin(FilterSet):
    user_age = NumberFilter(field_name='user_age', method='filter_user_age')

    def filter_user_age(self, queryset, name, value):
        return queryset.filter(
            Q(min_age=None) | Q(min_age__lte=value),
            Q(max_age=None) | Q(max_age__gte=value),
        )

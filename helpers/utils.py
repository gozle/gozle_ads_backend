import random

from django.db.models import QuerySet


def ads_data(queryset: QuerySet, qs_count: int, serializer_class):
    if qs_count >= 5:
        qs = queryset.order_by("score")[:5]
        qs_list = [x for x in qs]
        queryset = random.choice(qs_list)
    elif qs_count < 5 and qs_count != 1:
        queryset = queryset.order_by("?").first()

    serializer = serializer_class(queryset)
    queryset.view_count_increase()
    return serializer.data

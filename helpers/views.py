from django.utils import timezone

from datetime import timedelta

from django_celery_beat.models import ClockedSchedule
from rest_framework.response import Response


def ads_data(model, serializer_class):
    queryset_count = model.objects.filter(status="active").count()
    if queryset_count != 0:
        queryset = (model.objects.filter(status="active")
                    .order_by("view_count")
                    .first())
        serializer = serializer_class(queryset)
        queryset.count_increase()
        return Response(serializer.data)

    return Response(status=204)


def create_clock_schedule(duration: int):
    timedelta_seconds = timedelta(seconds=duration)
    clocked_time = timezone.now() + timedelta_seconds
    return ClockedSchedule.objects.create(
        clocked_time=clocked_time
    )

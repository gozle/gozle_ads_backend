import json
from datetime import timedelta
from uuid import uuid4

from django.utils import timezone

from django_celery_beat.models import ClockedSchedule, PeriodicTask
from rest_framework.response import Response

from ads.models import Banner


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


def create_hide_banner_task(schedule, uuid):
    periodic_task = PeriodicTask.objects.create(
        clocked=schedule,
        name=f"{uuid4()}",
        task="ads.tasks.hide_banner",
        kwargs=json.dumps({
            "uuid": str(uuid)
        }),
        enabled=True,
        one_off=True,
    )
    return periodic_task


def create_hide_imput_task(schedule, uuid):
    periodic_task = PeriodicTask.objects.create(
        clocked=schedule,
        name=f"{uuid4()}",
        task="ads.tasks.hide_imput",
        kwargs=json.dumps({
            "uuid": str(uuid)
        }),
        enabled=True,
        one_off=True,
    )
    return periodic_task


def create_hide_video_task(schedule, uuid):
    periodic_task = PeriodicTask.objects.create(
        clocked=schedule,
        name=f"{uuid4()}",
        task="ads.tasks.hide_video",
        kwargs=json.dumps({
            "uuid": str(uuid)
        }),
        enabled=True,
        one_off=True,
    )
    return periodic_task

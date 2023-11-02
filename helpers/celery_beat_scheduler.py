import json
from datetime import timedelta
from uuid import uuid4, UUID

from django.utils import timezone

from django_celery_beat.models import ClockedSchedule, PeriodicTask

ADS_HIDE_TASK_NAMES = {
    "banner": "ads.tasks.hide_banner",
    "imput": "ads.tasks.hide_imput",
    "video": "ads.tasks.hide_video",
}


def create_clock_schedule(duration: int):
    timedelta_seconds = timedelta(seconds=duration)
    clocked_time = timezone.now() + timedelta_seconds
    return ClockedSchedule.objects.create(
        clocked_time=clocked_time
    )


def create_status_hide_task(schedule, uuid: UUID, task_name: str):
    periodic_task = PeriodicTask.objects.create(
        clocked=schedule,
        name=f"{uuid4()}",
        task=task_name,
        kwargs=json.dumps({
            "uuid": str(uuid)
        }),
        enabled=True,
        one_off=True,
    )
    return periodic_task

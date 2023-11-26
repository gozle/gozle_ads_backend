import json
from datetime import datetime, timezone, timedelta
from uuid import UUID, uuid4

from django.utils import timezone
from django_celery_beat.models import CrontabSchedule, ClockedSchedule, PeriodicTask


ADS_SET_STATUS_TASK_NAMES = {
    "banner": "ads.tasks.set_status_banner",
    "imput": "ads.tasks.set_status_imput",
    "video": "ads.tasks.set_status_video",
}


class Schedule:

    @staticmethod
    def create_clock_schedule(seconds: int):
        timedelta_seconds = timedelta(seconds=seconds)
        clocked_time = timezone.now() + timedelta_seconds
        clocked_schedule, _ = ClockedSchedule.objects.get_or_create(
            clocked_time=clocked_time
        )
        return clocked_schedule

    @staticmethod
    def create_crontab_schedule(date_time: datetime):
        crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=date_time.minute,
            hour=date_time.hour,
            day_of_week=date_time.weekday,
            day_of_month=date_time.day,
            month_of_year=date_time.month,
        )
        return crontab_schedule


class Task:

    @staticmethod
    def create_status_hide_task(schedule, uuid: UUID, task_name: str, status: str):
        periodic_task = PeriodicTask.objects.create(
            clocked=schedule,
            name=f"{uuid4()}",
            task=task_name,
            kwargs=json.dumps({
                "uuid": str(uuid),
                "status": status,
            }),
            enabled=True,
            one_off=True,
        )
        return periodic_task


def create_set_status_task(
    date: datetime,
    uuid: uuid4,
    status: str,
    ads_type: str
):
    now = timezone.now()
    seconds = (date - now).seconds

    # Creating set status task
    schedule = Schedule.create_clock_schedule(seconds=seconds)
    task = Task.create_status_hide_task(
        schedule=schedule,
        uuid=uuid,
        status=status,
        task_name=ADS_SET_STATUS_TASK_NAMES[ads_type]
    )
    return task

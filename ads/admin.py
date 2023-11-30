from django.contrib import admin
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta

from .models import Banner, Device, Imput, Video
from helpers.celery_beat_scheduler import ADS_SET_STATUS_TASK_NAMES, Task, Schedule
from helpers.converters import convert_to_m3u8
from helpers.validators import dates_are_valid


class AdsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change) -> None:
        now = timezone.now() + timedelta(seconds=20)
        if now >= obj.starts_at:
            obj.status = obj.Statuses.ACTIVE

        return super().save_model(request, obj, form, change)

    exclude = ("published_at", "deleted_at")


class VideoAdmin(AdsAdmin):
    def save_model(self, request, obj, form, change) -> None:
        now = timezone.now() + timedelta(seconds=60)
        model_name = obj._meta.model_name

        if not dates_are_valid(start_data=obj.starts_at, end_data=obj.ends_at):
            raise ValidationError("Start or End dates are not valid!")

        if now > obj.starts_at:
            schedule = Schedule.create_clock_schedule(seconds=60)
            task = Task.create_set_status_task(
                schedule=schedule,
                status="active",
                task_name=ADS_SET_STATUS_TASK_NAMES[model_name],
                uuid=obj.uuid
            )

        super().save_model(request, obj, form, change)
        convert_to_m3u8.delay(obj.uuid)


admin.site.register(Banner, AdsAdmin)
admin.site.register(Device)
admin.site.register(Imput, AdsAdmin)
admin.site.register(Video, VideoAdmin)

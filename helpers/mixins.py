from helpers.celery_beat_scheduler import (
    ADS_HIDE_TASK_NAMES,
    create_clock_schedule,
    create_status_hide_task
)


class TaskCreatorMixin:

    def save(self, *args, **kwargs):
        if self.is_active:
            duration = self.duration
            uuid = self.uuid
            # Creating Celery task which hide object's status to hidden
            schedule = create_clock_schedule(duration=duration)
            task = create_status_hide_task(
                schedule=schedule,
                uuid=uuid,
                task_name=ADS_HIDE_TASK_NAMES[self._meta.verbose_name.lower()]
            )
        return super().save(*args, **kwargs)

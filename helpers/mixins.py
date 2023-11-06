from helpers.celery_beat_scheduler import (ADS_HIDE_TASK_NAMES,
                                           create_clock_schedule,
                                           create_status_hide_task)


class TaskCreatorMixin:

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        duration = response.data["duration"]
        uuid = response.data["uuid"]
        # Creating Celery task which hide object's status to hidden
        schedule = create_clock_schedule(duration=duration)
        task = create_status_hide_task(
            schedule=schedule,
            uuid=uuid,
            task_name=ADS_HIDE_TASK_NAMES[self.ads_type]
        )
        return response
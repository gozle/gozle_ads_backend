from helpers.utils import (
    create_clock_schedule,
    create_status_hide_task,
    HIDE_TASK_NAMES
)


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
            task_name=HIDE_TASK_NAMES[f"{self.adv_type}"]
        )
        return response
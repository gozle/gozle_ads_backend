from django.core.exceptions import ValidationError

from .celery_beat_scheduler import create_set_status_task
from .validators import dates_are_valid


class TaskCreatorMixin:

    def save(self, *args, **kwargs):
        _id = self.id
        if not _id:
            starts_at = self.starts_at
            ends_at = self.ends_at
            uuid = self.uuid
            ads_type = self._meta.verbose_name.lower()
            if dates_are_valid(start_data=starts_at, end_data=ends_at):

                if self.status.lower() != "active":
                    # Creating Celery task which sets object's status to active
                    create_set_status_task(
                        ads_type=ads_type,
                        date=starts_at,
                        status="active",
                        uuid=uuid,
                    )

                # Creating Celery task which sets object's status to hidden
                create_set_status_task(
                    ads_type=ads_type,
                    date=ends_at,
                    status="hidden",
                    uuid=uuid,
                )

                return super().save(*args, **kwargs)

            raise ValidationError("Start or End dates are not valid!")

        return super().save(*args, **kwargs)

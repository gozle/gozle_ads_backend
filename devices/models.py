from django.db import models
from django.utils.translation import gettext as _

from multiselectfield import MultiSelectField


class Device(models.Model):
    class Platforms(models.TextChoices):
        APP = "app", _("App")
        WEB = "web", _("Web")

    name = models.CharField(max_length=50)
    platforms = MultiSelectField(choices=Platforms.choices, max_length=10)

    def __str__(self):
        return f"{self.name}"

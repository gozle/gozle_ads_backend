from django.db import models
from django.utils.translation import gettext as _


class Device(models.Model):
    class Platforms(models.TextChoices):
        WEB = "web", _("Web")
        APP = "app", _("App")

    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=10, choices=Platforms.choices)

    def __str__(self):
        return f"{Device.Platforms(self.platform).label} {self.name}"

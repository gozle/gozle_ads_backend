import uuid

from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _

from multiselectfield import MultiSelectField

from .fields import WEBPField


def banner_folder(instance, filename):
    return 'banner/{}.webp'.format(uuid.uuid4().hex)


def video_folder(instance, filename):
    return 'video/{}.webp'.format(uuid.uuid4().hex)


def imput_folder(instance, filename):
    return 'imput/{}.webp'.format(uuid.uuid4().hex)


class Device(models.Model):
    class Platforms(models.TextChoices):
        APP = "app", _("App")
        WEB = "web", _("Web")

    name = models.CharField(max_length=50)
    platforms = MultiSelectField(choices=Platforms.choices, max_length=10)

    def __str__(self):
        return f"{self.name}"


class AdvertisementModelMixin(models.Model):
    class Statuses(models.TextChoices):
        ACTIVE = "active", _("Active")
        HIDDEN = "hidden", _("Hidden")
        DELETED = "deleted", _("Deleted")
        TEST = "test", _("Test")

    link = models.URLField()
    view_count = models.PositiveIntegerField(default=0)
    age_from = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])
    age_to = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])
    devices = models.ManyToManyField(Device, verbose_name="platforms",)
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=Statuses.choices, default=Statuses.ACTIVE)
    uuid = models.UUIDField(default=uuid.uuid4)

    def count_increase(self):
        self.view_count += 1
        self.save()
    
    def set_as_hidden(self):
        self.status = self.Statuses.HIDDEN
        self.save()

    class Meta:
        abstract = True


class Banner(AdvertisementModelMixin):
    text = models.CharField(max_length=255)
    description = models.TextField()
    image = WEBPField(
        verbose_name='Image',
        upload_to=banner_folder,
    )

    def __str__(self):
        return f"{self.id}. {self.text}"


class Video(AdvertisementModelMixin):
    text = models.CharField(max_length=255)
    description = models.TextField()
    image = WEBPField(
        verbose_name='Image',
        upload_to=video_folder,
    )
    video = models.FileField(upload_to='video/',
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return f"{self.id}. {self.text}"


class Imput(AdvertisementModelMixin):
    image = WEBPField(
        verbose_name='Image',
        upload_to=imput_folder,
    )

    def __str__(self):
        return f"{self.link}"

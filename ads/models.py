from uuid import uuid4

from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator
)
from django.db import models
from django.utils.translation import gettext as _

from multiselectfield import MultiSelectField

from .fields import WEBPField


def banner_folder(instance, filename):
    return 'banner/{}.webp'.format(uuid4().hex)


def video_folder(instance, filename):
    return 'video/{}.webp'.format(uuid4().hex)


def imput_folder(instance, filename):
    return 'imput/{}.webp'.format(uuid4().hex)


class Device(models.Model):
    class Platforms(models.TextChoices):
        APP = "app", _("App")
        WEB = "web", _("Web")

    name = models.CharField(max_length=50)
    platforms = MultiSelectField(
        max_length=10,
        choices=Platforms.choices
    )

    def __str__(self):
        return f"{self.name}"


class AdvertisementQueryset(models.QuerySet):
    def active_advertisements(self) -> models.QuerySet:
        return self.filter(
            status=AdvertisementModelMixin.Statuses.ACTIVE
        )


class AdvertisementModelMixin(models.Model):
    class Statuses(models.TextChoices):
        ACTIVE = "active", _("Active")
        HIDDEN = "hidden", _("Hidden")
        DELETED = "deleted", _("Deleted")
        TEST = "test", _("Test")

    objects = AdvertisementQueryset.as_manager()

    link = models.URLField()
    view_count = models.PositiveIntegerField(default=0)
    age_from = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(80)
        ]
    )
    age_to = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(80)
        ]
    )
    devices = models.ManyToManyField(
        Device,
        verbose_name="advertisement"
    )
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=30,
        choices=Statuses.choices,
        default=Statuses.ACTIVE
    )
    uuid = models.UUIDField(default=uuid4)

    def view_count_increase(self):
        self.view_count += 1
        self.save()

    def set_as_active(self):
        self.status = self.Statuses.ACTIVE
        self.save()

    def set_as_hidden(self):
        self.status = self.Statuses.HIDDEN
        self.save()

    def set_as_deleted(self):
        self.status = self.Statuses.DELETED
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
    video = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(
            allowed_extensions=[
                'MOV',
                'avi',
                'mp4',
                'webm',
                'mkv'
            ])
        ]
    )
    skip_duration = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(3),
            MaxValueValidator(15)
        ]
    )

    def __str__(self):
        return f"{self.id}. {self.text}"


class Imput(AdvertisementModelMixin):
    image = WEBPField(
        verbose_name='Image',
        upload_to=imput_folder,
    )

    def __str__(self):
        return f"{self.link}"

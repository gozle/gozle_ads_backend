from uuid import uuid4

from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from multiselectfield import MultiSelectField

from .fields import WEBPField
from .ranker import Ranker


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


class AdsRanker:
    def __init__(self, queryset):
        self.queryset = queryset

    def get_score(self):
        return Ranker.get_score(
            current_time=timezone.now(),
            published_date=self.queryset.published_at,
            view_count=self.queryset.view_count,
        )


class AdvertisementQueryset(models.QuerySet):
    def active_advertisements(self) -> models.QuerySet:
        return self.filter(
            status=AdvertisementModelMixin.Statuses.ACTIVE
        )

    def five_low_score_ads(self) -> models.QuerySet:
        if self.all().count() < 5:
            return self.all()
        return (
            self.all()
            .order_by("score")[:5]
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
    published_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=30,
        choices=Statuses.choices,
        default=Statuses.ACTIVE
    )
    uuid = models.UUIDField(default=uuid4)
    score = models.IntegerField(default=0)

    @property
    def is_active(self):
        return self.status == self.Statuses.ACTIVE

    @property
    def is_deleted(self):
        return self.status == self.Statuses.DELETED

    @property
    def is_for_test(self):
        return self.status == self.Statuses.TEST

    @property
    def is_hidden(self):
        return self.status == self.Statuses.HIDDEN

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
        self.deleted_at = timezone.now()
        self.save()

    def save(self, *args, **kwargs) -> None:
        if not self.published_at and not self.is_hidden:
            self.published_at = timezone.now()

        if not self.deleted_at and self.is_deleted:
            self.deleted_at = timezone.now()

        return super().save(*args, **kwargs)

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

    class Meta:
        verbose_name = "banner"


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

    class Meta:
        verbose_name = "video"


class Imput(AdvertisementModelMixin):
    image = WEBPField(
        verbose_name='Image',
        upload_to=imput_folder,
    )

    def __str__(self):
        return f"{self.link}"

    class Meta:
        verbose_name = "imput"

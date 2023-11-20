import os
from uuid import uuid4

from django.core.files.uploadedfile import TemporaryUploadedFile
from django.core.files.storage import default_storage
from django.core.validators import (FileExtensionValidator, MaxValueValidator,
                                    MinValueValidator)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from .fields import WEBPField
from .ranker import Ranker

from helpers.converters import convert_to_m3u8
from helpers.mixins import TaskCreatorMixin
from helpers.utils import move_ts_file
from locations.models import Province


def banner_folder(instance, filename):
    return 'banner/{}.webp'.format(uuid4().hex)


def video_folder(instance, filename):
    return 'video/images/{}.webp'.format(uuid4().hex)


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


class AdvertisementModelMixin(TaskCreatorMixin, models.Model):
    class Statuses(models.TextChoices):
        ACTIVE = "active", _("Active")
        HIDDEN = "hidden", _("Hidden")
        DELETED = "deleted", _("Deleted")
        TEST = "test", _("Test")

    objects = AdvertisementQueryset.as_manager()

    link = models.URLField()
    view_count = models.PositiveIntegerField(default=0)
    min_age = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(80)
        ]
    )
    max_age = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(80)
        ]
    )
    devices = models.ManyToManyField(
        Device,
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
    uuid = models.UUIDField(default=uuid4, unique=True)
    score = models.IntegerField(default=0)
    provinces = models.ManyToManyField(Province)

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
    cycle_duration = models.PositiveIntegerField(
        validators=[
            MinValueValidator(60)
        ],
        default=180
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
        upload_to='video/videos/',
        validators=[FileExtensionValidator(
            allowed_extensions=[
                'MOV',
                'avi',
                'mp4',
                'webm',
                'mkv',
                'm'
            ])
        ]
    )
    skip_duration = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(3),
            MaxValueValidator(20)
        ]
    )

    def save(self, *args, **kwargs) -> None:
        _id = self.id
        super().save(*args, **kwargs)

        if not _id:
            video_path, output_path = convert_to_m3u8(self.video)

            with open(output_path, 'rb') as source_file:
                data = source_file.read()

            # Create a temporary file and write data to it
            temp_file = TemporaryUploadedFile(
                name=output_path,
                size=os.path.getsize(output_path),
                content_type="video/x-mpegURL",
                charset="utf-8"
            )
            temp_file.write(data)
            temp_file.seek(0)  # Set the pointer to the beginning of the file

            # Saves new converted file
            self.video = temp_file
            self.save()

            # Closes temporary file
            temp_file.close()

            # Moves ts file with m3u8 file
            move_ts_file(self.video.name)

            # Deletes a temporary file
            default_storage.delete(video_path)
            default_storage.delete(output_path)

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

import uuid

from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models

from .fields import WEBPField


def banner_folder(instance, filename):
    return 'banner/{}.webp'.format(uuid.uuid4().hex)


def video_folder(instance, filename):
    return 'video/{}.webp'.format(uuid.uuid4().hex)


def imput_folder(instance, filename):
    return 'imput/{}.webp'.format(uuid.uuid4().hex)


class Banner(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    image = WEBPField(
        verbose_name='Image',
        upload_to=banner_folder,
    )
    link = models.URLField()
    view_count = models.PositiveIntegerField(default=0)
    age_from = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])
    age_to = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])

    def __str__(self):
        return f"{self.id}. {self.text}"

    def count_increase(self):
        self.view_count += 1
        self.save()


class Video(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    image = WEBPField(
        verbose_name='Image',
        upload_to=video_folder,
    )
    video = models.FileField(upload_to='video/',
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    link = models.URLField()
    view_count = models.PositiveIntegerField(default=0)
    age_from = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])
    age_to = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])

    def __str__(self):
        return f"{self.id}. {self.text}"

    def count_increase(self):
        self.view_count += 1
        self.save()


class Imput(models.Model):
    image = WEBPField(
        verbose_name='Image',
        upload_to=imput_folder,
    )
    link = models.URLField()
    view_count = models.PositiveIntegerField(default=0)
    age_from = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])
    age_to = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(80)])

    def __str__(self):
        return f"{self.id}"

    def count_increase(self):
        self.view_count += 1
        self.save()

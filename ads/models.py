import uuid

from django.core.validators import FileExtensionValidator
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
        height_field='height',
        width_field='width'
    )
    link = models.URLField()

    def __str__(self):
        return self.text
    


class Video(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    image = WEBPField(
        verbose_name='Image',
        upload_to=video_folder,
    )
    video = models.FileField(upload_to='video/',
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    link = models.URLField()

    def __str__(self):
        return self.text
    


class Imput(models.Model):
    image = WEBPField(
        verbose_name='Image',
        upload_to=imput_folder,
        height_field='height',
        width_field='width'
    )
    link = models.URLField()

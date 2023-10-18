"""Celery tasks."""

from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

from gozle_ads.settings.base import TIME_ZONE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gozle_ads.settings")
app = Celery("gozle_ads")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.timezone = TIME_ZONE
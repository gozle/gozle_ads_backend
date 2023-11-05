"""Celery tasks."""

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

from gozle_ads.settings.base import TIME_ZONE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gozle_ads.settings")
app = Celery("gozle_ads", include=['core.tasks'])

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.timezone = TIME_ZONE

app.conf.beat_schedule = {
    "banner_changer_socket": {
        "task": "ads.tasks.banner_socket",
        "schedule": crontab(minute="*/1"),
    },
    # Every hour
    "banner_ranker": {
        "task": "core.tasks.update_banner_score",
        "schedule": crontab(hour="*/1", minute="1"),
    },
    "video_ranker": {
        "task": "core.tasks.update_video_score",
        "schedule": crontab(hour="*/1", minute="2"),
    },
    "imput_ranker": {
        "task": "core.tasks.update_imput_score",
        "schedule": crontab(hour="*/1", minute="3"),
    },
}

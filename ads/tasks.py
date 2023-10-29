from celery import shared_task

from ads.models import (
    Banner,
    Imput,
    Video
)


@shared_task
def hide_banner(uuid):
    queryset = Banner.objects.get(uuid=uuid)
    queryset.set_as_hidden()


@shared_task
def hide_imput(uuid):
    queryset = Imput.objects.get(uuid=uuid)
    queryset.set_as_hidden()


@shared_task
def hide_video(uuid):
    queryset = Video.objects.get(uuid=uuid)
    queryset.set_as_hidden()

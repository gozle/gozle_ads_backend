from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

from ads.models import Banner, Imput, Video
from ads.serializers import BannerSerializer
from helpers.utils import ads_data


@shared_task
def set_status_banner(uuid, status):
    qs = Banner.objects.get(uuid=uuid)
    if status.lower() == "active":
        qs.set_as_active()
    else:
        qs.set_as_hidden()


@shared_task
def set_status_imput(uuid, status):
    qs = Imput.objects.get(uuid=uuid)
    if status.lower() == "active":
        qs.set_as_active()
    else:
        qs.set_as_hidden()
    print("TASK CREATED")


@shared_task
def set_status_video(uuid, status: str):
    qs = Video.objects.get(uuid=uuid)
    if status.lower() == "active":
        qs.set_as_active()
    else:
        qs.set_as_hidden()


@shared_task
def banner_socket():
    channel_layer = get_channel_layer()
    qs_count = Banner.objects.count()
    if qs_count != 0:
        data = ads_data(Banner.objects.all(), qs_count, BannerSerializer)
        if data:
            async_to_sync(channel_layer.group_send)(
                "banner_changer_group",
                {
                    "type": "banner_ads_socket",
                    "value": data
                }
            )
            return "Banner succesfully sent to the websocket"
    return "No banner found"

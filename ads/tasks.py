from asgiref.sync import async_to_sync

from celery import shared_task
from channels.layers import get_channel_layer

from ads.models import Banner, Imput, Video
from ads.serializers import BannerSerializer
from helpers.utils import ads_data


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


@shared_task
def banner_socket():
    channel_layer = get_channel_layer()
    data = ads_data(Banner, BannerSerializer)
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

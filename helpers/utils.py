import random
import shutil
import time

from django.conf import settings
from django.db.models import QuerySet

from ads.models import Video


def ads_data(
    queryset: QuerySet,
    qs_count: int,
    serializer_class,
    request=None
):
    if qs_count >= 5:
        qs = queryset.order_by("score")[:5]
        qs_list = [x for x in qs]
        queryset = random.choice(qs_list)
    elif qs_count < 5 and qs_count != 1:
        queryset = queryset.order_by("?").first()
    else:
        queryset = queryset.first()

    serializer = serializer_class(queryset, context={"request": request})
    queryset.view_count_increase()
    return serializer.data


def move_ts_file(video_file_name):
    ts_file_name = f"{video_file_name.split('.')[0].split('/')[-1]}0.ts"
    ts_file_path = f"{settings.MEDIA_ROOT}/{ts_file_name}"
    ts_file_move_path = f"{settings.MEDIA_ROOT}/video/videos/"
    shutil.move(ts_file_path, ts_file_move_path)


def get_video_qs(uuid):
    while True:
        try:
            return Video.objects.get(uuid=uuid)
        except Video.DoesNotExist:
            time.sleep(2)
            continue

from celery import shared_task

from ads.models import (
    AdsRanker,
    Banner,
    Imput,
    Video
)
from helpers.cache import ads_caching


@shared_task
def update_banner_score():
    banners = Banner.objects.active_advertisements()
    for banner in banners:
        score = AdsRanker(banner).get_score()
        banner.score = score

    Banner.objects.bulk_update(banners, ["score"])
    ads_caching(Banner)
    return "Banner score successfully updated"


@shared_task
def update_imput_score():
    imputs = Imput.objects.active_advertisements()
    for imput in imputs:
        score = AdsRanker(imput).get_score()
        imput.score = score

    Imput.objects.bulk_update(imputs, ["score"])
    ads_caching(Imput)
    return "Imput score successfully updated"


@shared_task
def update_video_score():
    videos = Video.objects.active_advertisements()
    for video in videos:
        score = AdsRanker(video).get_score()
        video.score = score

    Video.objects.bulk_update(videos, ["score"])
    ads_caching(Video)
    return "Video score successfully updated"

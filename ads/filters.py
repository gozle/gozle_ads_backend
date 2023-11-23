from helpers.filters import AdvertisementFilterSetMixin

from .models import Banner, Imput, Video


class BannerFilterSet(AdvertisementFilterSetMixin):

    class Meta:
        model = Banner
        fields = ['user_age', 'provinces', 'devices']


class ImputFilterSet(AdvertisementFilterSetMixin):

    class Meta:
        model = Imput
        fields = ['user_age', 'provinces', 'devices']


class VideoFilterSet(AdvertisementFilterSetMixin):

    class Meta:
        model = Video
        fields = ['user_age', 'provinces', 'devices']

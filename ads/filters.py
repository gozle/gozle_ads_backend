from helpers.filters import AdvertisementFilterSetMixin

from .models import Banner, Imput, Video


class BannerFilterSet(AdvertisementFilterSetMixin):

    class Meta:
        model = Banner
        fields = ['birth_year', 'provinces', 'devices', 'cities']


class ImputFilterSet(AdvertisementFilterSetMixin):

    class Meta:
        model = Imput
        fields = ['birth_year', 'provinces', 'devices', 'cities']


class VideoFilterSet(AdvertisementFilterSetMixin):

    class Meta:
        model = Video
        fields = ['birth_year', 'provinces', 'devices', 'cities']

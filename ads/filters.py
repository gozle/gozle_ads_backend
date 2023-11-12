from django_filters import ModelMultipleChoiceFilter

from helpers.filters import AdvertisementFilterSetMixin

from .models import Banner, Imput, Video


class BannerFilterSet(AdvertisementFilterSetMixin):
    provinces = ModelMultipleChoiceFilter(
        field_name='provinces',
        to_field_name='id',
        queryset=Banner.objects.active_advertisements(),
    )

    class Meta:
        model = Banner
        fields = ['user_age', 'provinces']


class ImputFilterSet(AdvertisementFilterSetMixin):
    provinces = ModelMultipleChoiceFilter(
        field_name='provinces',
        to_field_name='id',
        queryset=Imput.objects.active_advertisements(),
    )

    class Meta:
        model = Imput
        fields = ['user_age', 'provinces']


class VideoFilterSet(AdvertisementFilterSetMixin):
    provinces = ModelMultipleChoiceFilter(
        field_name='provinces',
        to_field_name='id',
        queryset=Video.objects.active_advertisements(),
    )

    class Meta:
        model = Video
        fields = ['user_age', 'provinces']

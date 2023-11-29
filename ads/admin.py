from django.contrib import admin
from django.utils import timezone
from datetime import timedelta

from .models import Banner, Device, Imput, Video
from helpers.converters import convert_to_m3u8


class AdsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change) -> None:
        starts_at = obj.starts_at
        now = timezone.now() + timedelta(seconds=20)
        if now >= starts_at:
            obj.status = obj.Statuses.ACTIVE

        return super().save_model(request, obj, form, change)

    exclude = ("published_at", "deleted_at")


class VideoAdmin(AdsAdmin):
    def save_model(self, request, obj, form, change) -> None:
        super().save_model(request, obj, form, change)
        convert_to_m3u8.delay(obj.uuid)


admin.site.register(Banner, AdsAdmin)
admin.site.register(Device)
admin.site.register(Imput, AdsAdmin)
admin.site.register(Video, VideoAdmin)
